<template>
  <div id="dwv" style="height: 80%;width: 100%;overflow-y: hidden;">
    <md-progress-bar md-mode="determinate" :md-value="loaded"></md-progress-bar>
    <div class="button-row">
      <el-button class="md-raised md-primary" value="ZoomAndPan" v-on:click="onClick">Scroll</el-button>
<!--      <md-button class="md-raised md-primary" value="WindowLevel" v-on:click="onClick">WindowLevel</md-button>-->
<!--            <md-button class="md-raised md-primary" value="ZoomAndPan" v-on:click="onClick">ZoomAndPan</md-button>-->
<!--            <md-button class="md-raised md-primary" value="Draw" v-on:click="onClick">Draw</md-button>-->
    </div>
    <div class="layerContainer">
      <div class="dropBox" >
        <span style="position: relative;line-height: 400px;">拖拽到此处上传图片</span>
      </div>
      <canvas class="imageLayer" >仅适用于兼容HTML5的浏览器……</canvas>
      <div class="drawDiv"></div>
    </div>
<!--    <div class="legend">{{ legend }}</div>-->
  </div>
</template>

<script>
  // import
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
    name: 'dragImg',
    props:{
      target:{}
    },
    data: function () {
      return {
        legend:  dwv.getVersion() ,
        dwvApp: null,
        loaded: 0
      }
    },
    mounted () {
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
    methods: {
      onClick: function (event) {
        console.log(this.target)
        this.dwvApp.onChangeTool(event)
      }
    }
  }
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
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
</style>
