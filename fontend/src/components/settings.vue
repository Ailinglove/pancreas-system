<template>
  <!-- Main container div -->
  <div id="dwv" style="text-align: center">
<!--    <el-input style="width: 300px;" type="text" values="" />-->
    <span v-model="url">{{url}}</span>
      <el-button @click="loadDicom">加载图片</el-button>
      <div class="layerContainer">
          <canvas class="imageLayer"></canvas>
      </div>
  </div>
</template>
<script>
  // import
  import Vue from 'vue'
  import MdButton from 'vue-material'
  import dwv from 'dwv'


  Vue.use(MdButton)

  // gui overrides

  // decode query
  dwv.utils.decodeQuery = dwv.utils.base.decodeQuery
  // progress
  dwv.gui.displayProgress = function (percent) {}
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
  export default{
    data(){
      return{
          dwvapp:null,
        url:'api/showDiocm/1.dcm'
      }
    },
    mounted() {
       this.dwvapp=new dwv.App();
       this.dwvapp.init({
           "containerDivId": "dwv",
           "tools":['Scroll'],//序列图片
        });
        // load dicom data

    },
    methods:{
      loadDicom(){
        this.dwvapp.loadURLs(["api/showDiocm/1.dcm","api/showDiocm/2.dcm","api/showDiocm/3.dcm","api/showDiocm/4.dcm"
      ,"api/showDiocm/5.dcm","api/showDiocm/6.dcm","api/showDiocm/7.dcm"]);
        // this.dwvapp.loadFiles(["D:\\medicalImage\\changhaiData\\data\\20190000\\05398104_DAI ZU WANG_CT\\1.2.392.200036.9116.2.5.1.48.1224104463.1498111104.167062\\1.dcm"])

      }
    }
  }


</script>

<style>

</style>
