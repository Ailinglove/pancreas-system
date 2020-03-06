<template>
    <uploader
          :options="options"
          class="uploader-example"
          @file-progress="onFileProgress"
          @file-success="onFileSuccess"
          @file-error="onFileError"
        >
              <uploader-unsupport></uploader-unsupport>
              <uploader-drop>
                <p>上传病理图像</p>
                <uploader-btn>单个病理图像</uploader-btn>

                <uploader-btn :directory="true">批量上传</uploader-btn>
              </uploader-drop>
              <uploader-list></uploader-list>
        </uploader>
</template>

<script>
      export default {
    name:'pathoUploader',
    data () {
      return {
        options: {
          // https://github.com/simple-uploader/Uploader/tree/develop/samples/Node.js
          target: '/api/fileUploader/pathofile/',
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
      onFileProgress(rootFile, file, chunk) {
        console.log(`上传中 ${file}，chunk：${chunk.startByte / 1024 / 1024} ~ ${chunk.endByte / 1024 / 1024}`)
        console.log(chunk.file)
      },
      onFileSuccess(rootFile, file, response, chunk) {
        // let res = JSON.parse(response);

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
