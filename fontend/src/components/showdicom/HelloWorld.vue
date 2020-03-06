<template>
  <!-- Main container div -->
  <div style="padding-left: 10%">
    <header >
      <div class="el-icon-close" ></div>
    </header>
		<main>
			<div class="left main">
				<ul>
<!--          <li v-for="(item,index) in img" @click="loadDicom(item.imglist,item.name)" :class="{active: activeName == activeName}">{{item.name}}-->
					<li v-for="(item,index) in img" @click="loadDicom(item.imglist,item.name)" :class="{active: activeName == item.name}">{{item.name}}
          </li>
				</ul>
			</div>
			<div class="medium main">

        <span v-model="info" style="color: white;position: absolute;top:5px;left: 10px;">{{info}}</span>

        <div id="dwv" style="text-align: center;width: 600px;height: 600px;">
          <div class="layerContainer" style="height:520px;">
              <canvas class="imageLayer" width="600px" height="520px"></canvas>
          </div>
  </div>
      </div>
			<div class="right main">
        <el-button plain type="primary" effect="plain" v-for="tool in tools" :key="tool.type"
                   :label="tool" v-on:click="onChangeTool(tool.type)">{{tool.name}}</el-button>
            <el-button type="danger" v-on:click="onReset()" :disabled="!dataLoaded" plain>重置</el-button>
      </div>

		</main>

  </div>




</template>


<!--</script>-->
<script>
  // import
import Vue from 'vue'
import MdButton from 'vue-material'
import dwv from 'dwv'
import tagsTable from './tags-table'
  import {getImgURL} from '../../api/api'

Vue.use(MdButton)

// gui overrides

// decode query
dwv.utils.decodeQuery = dwv.utils.base.decodeQuery
// progress
dwv.gui.displayProgress = function () {}
// get element
dwv.gui.getElement = dwv.gui.base.getElement
// refresh element
dwv.gui.refreshElement = dwv.gui.base.refreshElement

// Image decoders (for web workers)
dwv.image.decoderScripts = {
  'jpeg2000': 'assets/dwv/decoders/pdfjs/decode-jpeg2000.js',
  'jpeg-lossless': 'assets/dwv/decoders/rii-mango/decode-jpegloss.js',
  'jpeg-baseline': 'assets/dwv/decoders/pdfjs/decode-jpegbaseline.js',
  'rle': 'assets/dwv/decoders/dwv/decode-rle.js'
}

export default {
  name: 'dwv',
  components: {
    tagsTable
  },
  data: function () {
    return {
      versions: {
        dwv: dwv.getVersion(),
        vue: Vue.version
      },
      value: '',
      radio: 'radio1',
      dwvApp: null,
      tools: [{type:'Scroll',name:'滚动'}, {type:'ZoomAndPan',name:'缩放'},{type: 'WindowLevel',name:'灰度值'}],
      tooltype: ['Scroll', 'ZoomAndPan', 'WindowLevel'],
      selectedTool: 'Select Tool',
      loadProgress: 0,
      dataLoaded: false,
      tags: null,
      showDicomTags: false,
      info:{modality:'',thickness:''},
      activeName: 'A1_Serial',

      img: [
        {name:'CT平扫',
          imglist: ['/api/showDiocm/imgData/0QG00000590/byMRI/20171021/ADC_Serial/thickness6.0/IM00001.dcm']
        },
        {name:'CT动脉期',
          imglist: ['/api/showDiocm/imgData/0QG00000590/byMRI/20171021/ADC_Serial/thickness6.0/IM00001.dcm']
        },
        {name:'CT门脉期',
          imglist: ['/api/showDiocm/imgData/0QG00000590/byMRI/20171021/ADC_Serial/thickness6.0/IM00001.dcm']
        },
        {name:'CT延迟期',
          imglist: ['/api/showDiocm/imgData/0QG00000590/byMRI/20171021/ADC_Serial/thickness6.0/IM00001.dcm'
]
        }
      ]
    }
  },
  mounted () {
    this.getImgURL()
    // create app
    this.dwvApp = new dwv.App()
    // initialise app
    this.dwvApp.init({
      'containerDivId': 'dwv',
      'tools': this.tooltype,
      'shapes': ['Ruler'],
      'isMobile': true
    })
    // progress
    var self = this
     // this.dwvApp.loadURLs(["/api/showDiocm/imgData/0QG00000590/byMRI/20171021/ADC_Serial/thickness6.0/IM00001.dcm"])
    this.dwvApp.addEventListener('load-end', function (/*event*/) {
      // set data loaded flag
      self.dataLoaded = true
      // set dicom tags
      self.tags = self.dwvApp.getTags()
      // set the selected tool
      if (self.dwvApp.isMonoSliceData() && self.dwvApp.getImage().getNumberOfFrames() === 1) {
        self.selectedTool = 'ZoomAndPan'
      } else {
        self.selectedTool = 'Scroll'
      }
    })

    //获取图像相关信息
     var url = "/api/showDiocm/imgData/0QG00000590/byMRI/20171021/ADC_Serial/thickness6.0/IM00001.dcm"

      var onload = function () {
          // setup the dicom parser
          var dicomParser = new dwv.dicom.DicomParser();
          // parse the buffer
          dicomParser.parse(this.response);

          // div to display text
          // var div = document.getElementById("tags");

          // get the raw dicom tags
          var rawTags = dicomParser.getRawDicomElements();
          // display the modality
          // div.appendChild(document.createTextNode(
          //     "Modality: " + rawTags.x00080060.value[0]
          // ));

          // break line
          // div.appendChild(document.createElement("br"));

          // get the wrapped dicom tags
          var tags = dicomParser.getDicomElements();
          // display the modality
          // div.appendChild(document.createTextNode(
          //     "Modality (bis): " + tags.getFromName("Modality")
          // ));
        console.log(tags)
          console.log(tags.getFromName("PatientAge"))
        console.log(tags.getFromName("SliceThickness"))
        console.log(tags.getFromName("Modality"))


      };

var request = new XMLHttpRequest();
request.open('GET', url, true);
request.responseType = "arraybuffer";
request.onload = onload;
request.send(null);
console.log('....',this.img)
    console.log(this.img[0])
// this.loadDicom(this.img[0],this.img[0].name)
  },
  methods: {
    onChangeTool(tool) {
       console.log(tool)
      this.selectedTool = tool

      this.dwvApp.onChangeTool({ currentTarget: { value: tool } })
    },
    onReset: function () {
      console.log('重置')
      this.dwvApp.onDisplayReset()
    },
    loadDicom(imglist,itemName){
      this.dwvApp.loadURLs(imglist)
      console.log('diaoyong')
   },
    getImgURL(){
      var postData={

      }
      getImgURL(postData).then((res)=>{

        this.img=res.data['url']
        this.activeName=this.img.name
        console.log(this.activeName)

      })
    }
  }}
</script>
<style scoped>
 header{background-color: #000000;width: 90%;height: 50px;line-height: 40px;}
 .el-icon-close{background-color: #8DC3FF;border-radius: 20px;width: 20px;height: 20px;line-height: 20px;
   position:relative;left:46%;}
 main{margin: auto;}
 .main{position:relative;height:800px;background-color: #000000;float: left;border: white solid 1px;text-align: center;}
 .left{width: 15%;padding-top: 5%;}
 .medium{width: 60%;padding-left:10%;padding-top: 5%}
 .right{width: 15%;padding-top: 5%;}
 li{background-color: #8DC3FF;height:50px;margin:10px;list-style: none;line-height: 50px;}
 li:hover{background-color:#ededed;}
 .el-button{width: 120px;margin: 10px;}
 .active{background-color: #ededed;}

</style>

<!--<template>-->
<!--  &lt;!&ndash; Main container div &ndash;&gt;-->


<!--        <div id="dwv" style="text-align: center;width: 600px;height: 600px;">-->
<!--          <div class="layerContainer" style="height:520px;">-->
<!--              <canvas class="imageLayer" width="600px" height="520px"></canvas>-->
<!--          </div>-->
<!--          <button @click="getImgUrl">dianji</button>-->
<!--  </div>-->




<!--</template>-->


<!--&lt;!&ndash;</script>&ndash;&gt;-->
<!--<script>-->
<!--  // import-->
<!--import Vue from 'vue'-->
<!--import MdButton from 'vue-material'-->
<!--import dwv from 'dwv'-->
<!--import tagsTable from './tags-table'-->
<!--import {getImgURL} from '../../api/api'-->
<!--Vue.use(MdButton)-->

<!--// gui overrides-->

<!--// decode query-->
<!--dwv.utils.decodeQuery = dwv.utils.base.decodeQuery-->
<!--// progress-->
<!--dwv.gui.displayProgress = function () {}-->
<!--// get element-->
<!--dwv.gui.getElement = dwv.gui.base.getElement-->
<!--// refresh element-->
<!--dwv.gui.refreshElement = dwv.gui.base.refreshElement-->

<!--// Image decoders (for web workers)-->
<!--dwv.image.decoderScripts = {-->
<!--  'jpeg2000': 'assets/dwv/decoders/pdfjs/decode-jpeg2000.js',-->
<!--  'jpeg-lossless': 'assets/dwv/decoders/rii-mango/decode-jpegloss.js',-->
<!--  'jpeg-baseline': 'assets/dwv/decoders/pdfjs/decode-jpegbaseline.js',-->
<!--  'rle': 'assets/dwv/decoders/dwv/decode-rle.js'-->
<!--}-->

<!--export default {-->
<!--  name: 'dwv',-->
<!--  components: {-->
<!--    tagsTable-->
<!--  },-->
<!--  data: function () {-->
<!--    return {-->
<!--      versions: {-->
<!--        dwv: dwv.getVersion(),-->
<!--        vue: Vue.version-->
<!--      },-->
<!--      value: '',-->
<!--      radio: 'radio1',-->
<!--      dwvApp: null,-->
<!--      tools: [{type:'Scroll',name:'滚动'}, {type:'ZoomAndPan',name:'缩放'},{type: 'WindowLevel',name:'灰度值'}],-->
<!--      tooltype: ['Scroll', 'ZoomAndPan', 'WindowLevel'],-->
<!--      selectedTool: 'Select Tool',-->
<!--      loadProgress: 0,-->
<!--      dataLoaded: false,-->
<!--      tags: null,-->
<!--      showDicomTags: false,-->

<!--activeName: '',-->


<!--    }-->

<!--  },-->
<!--  mounted () {-->

<!--    // create app-->
<!--    this.dwvApp = new dwv.App()-->
<!--    // initialise app-->
<!--    this.dwvApp.init({-->
<!--      'containerDivId': 'dwv',-->
<!--      'tools': this.tooltype,-->
<!--      'shapes': ['Ruler'],-->
<!--      'isMobile': true-->
<!--    })-->
<!--    // progress-->
<!--    var self = this-->
<!--    console.log('nnnn')-->
<!--     this.dwvApp.loadURLs(['api/showDiocm/imgData/0QG00000590/byMRI/20171021/ADC_Serial/thickness6.0/IM00005.dcm'])-->
<!--    this.dwvApp.addEventListener('load-end', function (/*event*/) {-->
<!--      // set data loaded flag-->
<!--      self.dataLoaded = true-->
<!--      // set dicom tags-->
<!--      self.tags = self.dwvApp.getTags()-->
<!--      // set the selected tool-->
<!--      if (self.dwvApp.isMonoSliceData() && self.dwvApp.getImage().getNumberOfFrames() === 1) {-->
<!--        self.selectedTool = 'ZoomAndPan'-->
<!--      } else {-->
<!--        self.selectedTool = 'Scroll'-->
<!--      }-->
<!--    })-->

<!--    //获取图像相关信息-->
<!--     var url = "api/showDiocm/imgData/0QG00000590/byMRI/20171021/ADC_Serial/thickness6.0/IM00005.dcm"-->


<!--var request = new XMLHttpRequest();-->
<!--request.open('GET', url, true);-->
<!--request.responseType = "arraybuffer";-->
<!--request.onload = onload;-->
<!--request.send(null);-->
<!--  },-->
<!--  methods: {-->
<!--     getImgUrl(){-->
<!--      // var postData={}-->
<!--      // getImgURL(postData).then((res)=>{-->
<!--      //   console.log(res)-->
<!--      //   console.log('niho')-->
<!--      // })-->
<!--       getImgURL().then((res)=>{-->
<!--        console.log(res)-->
<!--        console.log('niho')})-->
<!--       console.log('dianji')-->
<!--    }-->


<!--}}-->
<!--</script>-->
<!--<style scoped>-->
<!-- header{background-color: #000000;width: 90%;height: 50px;line-height: 40px;}-->
<!-- .el-icon-close{background-color: #8DC3FF;border-radius: 20px;width: 20px;height: 20px;line-height: 20px;-->
<!--   position:relative;left:46%;}-->
<!-- main{margin: auto;}-->
<!-- .main{position:relative;height:800px;background-color: #000000;float: left;border: white solid 1px;text-align: center;}-->
<!-- .left{width: 15%;padding-top: 5%;}-->
<!-- .medium{width: 60%;padding-left:10%;padding-top: 5%}-->
<!-- .right{width: 15%;padding-top: 5%;}-->
<!-- li{background-color: #8DC3FF;height:50px;margin:10px;list-style: none;line-height: 50px;}-->
<!-- li:hover{background-color:#ededed;}-->
<!-- .el-button{width: 120px;margin: 10px;}-->
<!-- .active{background-color: #ededed;}-->

<!--</style>-->
