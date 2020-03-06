<template>
  <div>
    <uploader
          :options="options"
          class="uploader-example"
          @file-progress="onFileProgress"
          @file-success="onFileSuccess"
          @file-error="onFileError"

        >
              <uploader-unsupport></uploader-unsupport>
              <uploader-drop >
                <p>上传影像图像</p>
                <uploader-btn>单个DCM图像</uploader-btn>

                <uploader-btn :directory="true" >批量上传</uploader-btn>
              </uploader-drop>
              <uploader-list></uploader-list>
        </uploader>
    <div id="popLayer"></div>
    <div id="popBox" >
      <div class="close">
        <a href="javascript:void(0)" @click="closeBox()">关闭</a>
      </div>
      <div class="content" style="line-height: 80px;">该病人已经存在于数据库中！</div></div>

  </div>

</template>

<script>
      export default {
    name:'imgUploader',
    data () {
      return {
        options: {
          // https://github.com/simple-uploader/Uploader/tree/develop/samples/Node.js
          target: '/api/fileUploader/imgfile/',
          testChunks: false,
          chunkSize:3*1024*1024,
          single:true,
          // processParams(params){//每次分片传给后台的参数
          //   return {
          //     name:params.filename,
          //     code:params.identifier,
          //     total:params.totalChunks,
          //     index:params.chunkNumber,
          //     chunk:params.chunks
          //   }
          //
          // }
        },
        attrs: {
          accept: 'image/*'
        },
        statusText: {
          success: '成功了',
          error: '出错了',
          uploading: '上传中',
          paused: '暂停中',
          waiting: '等待中'
        }
      }
    },
    methods:{
      popBox() {
        var popBox = document.getElementById("popBox");
        var popLayer = document.getElementById("popLayer");
        popBox.style.display = "block";
        popLayer.style.display = "block";
      } ,
      /*点击关闭按钮*/
      closeBox() {
        var popBox = document.getElementById("popBox");
        var popLayer = document.getElementById("popLayer");
        popBox.style.display = "none";
        popLayer.style.display = "none";
      },


      onFileProgress(rootFile, file, chunk) {
        // console.log(`上传中 ${file}，chunk：${chunk.startByte / 1024 / 1024} ~ ${chunk.endByte / 1024 / 1024}`)
        // console.log(chunk.file)
      },
      onFileSuccess(rootFile, file, response, chunk) {
        console.log('sss')
        this.popBox()
        // 服务器自定义的错误，这种错误是Uploader无法拦截的
        // if (!res.result) {
        //     this.$message({ message: res.message, type: 'error' });
        //     return
        // }

        // 如果服务端返回需要合并
        // if (res.needMerge) {
        //     api.mergeSimpleUpload({
        //         tempName: res.tempName,
        //         fileName: file.name,
        //         ...this.params,
        //     }).then(data => {
                // 文件合并成功

            // }).catch(e => {});
        // 不需要合并
        // } else {
        //     console.log('上传成功');
        // }
    },

  onFileError(rootFile, file, response, chunk) {
      console.log(error)
  },

    }
  }
</script>

<style>
  /*背景层*/

    #popBox {
      display: none;
      background-color: #FFFFFF;
      z-index: 11;
      width: 300px;
      height: 100px;
      position:fixed;
      top:0;
      right:0;
      left:100px;
      bottom:0;

      margin:auto;
    }
  #popBox .close{
    text-align: right;
    margin-right: 5px;
    background-color: #36a3f7;
  }         /*关闭按钮*/
  #popBox .close a {
    text-decoration: none;
    color: #ffffff;
  }


  .uploader-example {

    width: 500px;
    padding: 15px;
    margin: 40px 10px 10px 10px;
    font-size: 15px;
    box-shadow: 0 0 10px rgba(0, 0, 0, .4);
  }
  .uploader-example .uploader-btn {
    margin-right: 4px;
  }
  .uploader-example .uploader-list {
    max-height: 300px;
    overflow: auto;
    overflow-x: hidden;
    overflow-y: auto;
  }
  li{
    list-style: none;
  }
</style>
