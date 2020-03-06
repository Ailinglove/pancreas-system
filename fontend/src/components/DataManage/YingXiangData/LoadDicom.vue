<div>
  <nav></nav>
</div>
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
  name: 'LoadDicom',
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
      radio:'radio1',
      dwvApp: null,
      tools: ['Scroll', 'ZoomAndPan', 'WindowLevel'],
      selectedTool: 'Select Tool',
      loadProgress: 0,
      dataLoaded: false,
      tags: null,
      showDicomTags: false
    }
  },
  mounted () {
    // create app
    this.dwvApp = new dwv.App()
    // initialise app
    this.dwvApp.init({
      'containerDivId': 'dwv',
      'tools': this.tools,
      'shapes': ['Ruler'],
      'isMobile': true
    })
    // progress
    var self = this
     this.dwvApp.loadURLs(["api/showDiocm/1.dcm","api/showDiocm/2.dcm","api/showDiocm/3.dcm","api/showDiocm/4.dcm"
    ,"api/showDiocm/5.dcm","api/showDiocm/6.dcm","api/showDiocm/7.dcm"])
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
    loadDicom(){


      // this.dwvapp.loadFiles(["D:\\medicalImage\\changhaiData\\data\\20190000\\05398104_DAI ZU WANG_CT\\1.2.392.200036.9116.2.5.1.48.1224104463.1498111104.167062\\1.dcm"])-->

   }


}}
</script>
<style>
</style>
