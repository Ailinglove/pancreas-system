<template>
    <div class="dicom" ref="dicomImage"></div>
</template>
<script>
import * as cornerstone from "cornerstone-core";
import * as dicomParser from "dicom-parser";
// 不建议 npm 安装 cornerstoneWADOImageLoader 如果你做了 会很头疼
let cornerstoneWADOImageLoader = require('../../../static/dist/cornerstoneWADOImageLoader.js')
// import {cornerstoneWADOImageLoader} from "../../../static/dist/cornerstoneWADOImageLoader.js";
//指定要注册加载程序的基石实例
cornerstoneWADOImageLoader.external.cornerstone = cornerstone;
//配置 webWorker (必须配置)
//注意这里的路径问题  如果路径不对 cornerstoneWADOImageLoaderWebWorker 会报错 index.html Uncaught SyntaxError: Unexpected token <
var config = {
  webWorkerPath: "../../../static/dist/cornerstoneWADOImageLoaderWebWorker.js",
  taskConfiguration: {
    decodeTask: {
      codecsPath: "../../../static/dist/cornerstoneWADOImageLoaderCodecs.js"
    }
  }
};
cornerstoneWADOImageLoader.webWorkerManager.initialize(config);
export default {
    name: 'previewDicom',
    props: {
        imageId: {
            type: String,
            required: true
        }
    },
    data () {
        return {
        }
    },
    // watch:{
    //    imageId(newValue,oldValue){
    //     var url = `wadouri:${this.imageId}`;
    //     this.loadAndViewImage(url);
    //    }
    // },
    mounted() {
        var url = `wadouri:${this.imageId}`;

        this.loadAndViewImage(url);
    },
    methods: {
        loadAndViewImage(imageId) {
          console.log(this.imageId)
            //找到 要放置 Dicom Image 的元素
            // var element = document.getElementById("dicomImage");
            console.log(1334);
            let element = this.$refs.dicomImage
            cornerstone.enable(element)
            // cornerstone.loadAndCacheImage 函数 负责加载图形 需要 图像地址 imageId
            cornerstone.loadAndCacheImage(imageId).then(
                function(image) {
                    var viewport = cornerstone.getDefaultViewportForImage(element, image);
                    cornerstone.displayImage(element, image, viewport);
                },
                function(err) {
                    console.error(err)
                }
            );
        }
    }
}
</script>
<style scoped>
.dicom{
    height: 100%;
}
</style>
