<template>
  <div style="height: 100%;background-color:rgb(0,0,0);overflow: auto;width: 100%;">
    <div class="main" style="color: floralwhite;">
        <div class="leftbox" >
          <div class="desc leftitem" style="">
            <div style="width:100%;text-align: center"><strong style="text-align: center">{{title}}</strong></div>

            <div >{{rightData}}</div>
            分类结果：<span style="border-bottom: 1px solid gray">类别1</span>
            <p></p>
            分割结果：<span style="border-bottom: 1px solid gray">{{result}}</span>
            <br>
            <br>

            <br>
          </div>
          <div class="tools ">
            <el-button class="tool" value="Scroll" @click="onClick" :event="target">滚动切换</el-button>
            <el-button class="tool" value="WindowLevel" @click="onClick">调节透明度</el-button>
            <el-button class="tool" value="ZoomAndPan" @click="onClick">放大缩小</el-button>

            <el-button class="tool" value="WindowLevel" @click="onClick" style="color: brown">重置</el-button>
          </div>

      </div>
      <div class="box rightbox" >

        <div id="dwv" style="height: 80%;width: 100%;overflow-y: hidden;">
          <md-progress-bar md-mode="determinate" :md-value="loaded"></md-progress-bar>

          <div class="layerContainer">
            <div class="dropBox" >
              <span style="position: relative;line-height: 400px;">拖拽到此处上传图片</span>
            </div>
            <canvas class="imageLayer" >仅适用于兼容HTML5的浏览器……</canvas>
            <div class="drawDiv"></div>
          </div>
          <!--    <div class="legend">{{ legend }}</div>-->
        </div>


     </div>

    </div>
  </div>

</template>

<script>
  import dragImg from "@/views/expend/AICompute/analysis/dragImg";
  import Vue from 'vue'
  import MdButton from 'vue-material'
  import dwv from 'dwv'
  Vue.use(dwv)
  Vue.use(MdButton)

  // gui overrides

  // decode query(解码查询)
  dwv.utils.decodeQuery = dwv.utils.base.decodeQuery
  // progress
  dwv.gui.displayProgress = function () {}
  // window
  dwv.gui.getWindowSize = dwv.gui.base.getWindowSize
  // get element
  dwv.gui.getElement = dwv.gui.base.getElement
  // refresh element
  dwv.gui.refreshElement = dwv.gui.base.refreshElement

  // Image decoders (for web workers) 图像解码
  dwv.image.decoderScripts = {
    'jpeg2000': 'static/dwv/decoders/pdfjs/decode-jpeg2000.js',
    'jpeg-lossless': 'static/dwv/decoders/rii-mango/decode-jpegloss.js',
    'jpeg-baseline': 'static/dwv/decoders/pdfjs/decode-jpegbaseline.js'
  }
  export default {
    name: "segindex",
    components:{
      dragImg
    },
    data(){
      return {
        target:'',
        tumorType:[
          {value:'yixian',label:'胰腺数据'},
          {value:'naobu',label:'脑部数据'},
          {value:'yanbing',label:'致盲性眼病数据'},
          {value:'ruxian',label:'乳腺癌数据'},
          {value:'feijiejie',label:'肺结节数据'},

          {value:'changwei',label:'肠胃数据'},],
        tumorDic:{'naobu':'脑胶质瘤是因为大脑和脊髓胶质细胞癌变所产生的最常见的原发性颅脑恶性肿瘤。其发病率约占颅内肿瘤的35.2%~61.0%，由成胶质细胞衍化而来，具有发病率高、复发率高、死亡率高以及治愈率低的特点。',
          'yanbing':'青光眼是我国第一位的不可逆致盲性眼病。',
          'ruxian':'乳腺癌是发生在乳腺腺上皮组织的恶性肿瘤。乳腺癌中99%发生在女性，男性仅占1%。',
          'feijiejie':'肺结节病(sarcoidosis)是一种病因未明的多系统多器官的肉芽肿性疾病，常侵犯肺、双侧肺门淋巴结、眼、皮肤等器官，其胸部受侵率高达80%～90%。',
          'yixian':'胰腺癌，癌中之王，胰腺癌是一种恶性程度很高，诊断和治疗都很困难的消化道恶性肿瘤，约90%为起源于腺管上皮的导管腺癌。其发病率和死亡率近年来明显上升。5年生存率<1%，是预后最差的恶性肿瘤之一。',
          'changwei':'肠胃'
        },
        dataType:['JPG','DICM','NRRD'],
        selectedData:'',

        rightData:'',

        result:'待诊断',
        title:'胰腺数据',
        showimg:false,
        dwvApp: null,
        loaded: 0

      }
    },
    methods:{
      onClick: function (event) {
        console.log(this.target)
        this.dwvApp.onChangeTool(event)
      },
      getSelectedData(){
        let data=this.tumorDic[this.selectedData]
        this.rightData=data
        let titletmp=this.tumorType.filter((item,index)=>{
          return item.value===this.selectedData
        })
        this.title=titletmp[0]['label']
        console.log(this.title)
      },
      startAnalysis(){
        let that=this
        this.showimg=true
        setTimeout(function(){
          that.showimg=false
          that.result='见左图'
          console.log('nihao',this.showimg)
        },2000)


      }
    },
    mounted() {
      // create app
      this.dwvApp = new dwv.App()
      // initialise app
      this.dwvApp.init({
        'containerDivId': 'dwv',
        'fitToWindow': true,
        'tools': ['Scroll', 'ZoomAndPan', 'WindowLevel', 'Draw'],
        'shapes': ['Ruler'],
        'isMobile': true
      })
      // progress
      var self = this
      this.dwvApp.addEventListener('load-progress', function (event) {
        self.loaded = event.loaded
      })
    },
    created() {
      this.selectedData=this.tumorType[0].value
      this.rightData=this.tumorDic['yixian']
    }
  }
</script>

<style scoped>
  #dwv { font-family: Arial, Helvetica, sans-serif; }
  /* Layers */
  .dropBox{
    width: 500px;
    position: relative;
    top: 100px;
    border: 1px solid yellow;

  }
  .layerContainer {
    position: relative; padding: 0;
    margin: auto; text-align: center;
    overflow-y: hidden;
  }
  .imageLayer {
    z-index: 999;
    position: relative;
    top: 100px;
    width: 500px;
    left: 0px; }

  /* drag&drop */
  .dropBox {
    /*border: 5px dashed #ccc;*/
    margin: auto; text-align: center;
  }
  .dropBox.hover { border: 1px dashed #cc0; }
  span{
    color: white;
  }
  *{
    box-sizing: content-box;
  }

  .main{
    width: 100%;
    margin: 0 auto;height: 90%;
    display: flex;
    justify-content: space-between;
  }
  .box{
    height: 99%;
    border-right: 1px solid gray;
    border-left: 1px solid gray;

  }
  .desc{
   width: 100%;white-space: normal;
    padding: 20px 0;
    margin: 0 10px;
    text-align: left;
    color: gray;
  }
  .leftbox{
    display: flex;
    flex-direction: column;
    width: 30%;

    flex-wrap: wrap;
  }
  .rightbox{
    width: 70%;
    text-align: center;
    border: 10px solid gray;
    overflow-y: hidden;

  }
  select{
    height: 30px;
    width: 120px;
    font-size: 14px;
    border-radius: 2px;

  }
  .tools{

    display: flex;
    flex-direction: row;
    flex-wrap: wrap;
  }
  .tool{
    display: inline-block;
    width: 100px;
    margin: 5px;
  }

  /*.tool{*/
  /*  width: 150px;*/
  /*  height: 30px;*/
  /*  !*border-radius: 2px;*!*/
  /*  margin: 5px 20px 5px 0;*/
  /*  background-color:#cccccc;*/
  /*}*/
  .tool:hover{

    color: #2c3e50;
    background-color: darkgrey;
  }

</style>
