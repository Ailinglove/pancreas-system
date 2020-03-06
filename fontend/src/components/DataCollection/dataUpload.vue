<template>
  <div>
      <uploader :options="options" class="uploader-example" @file-progress="onFileProgress"
                @file-success="onFileSuccess" :file-status-text="fileStatusText" ref="assignBrowse"
                @file-added="onFileAdded" :auto-start="false"
          @file-error="onFileError">
              <uploader-unsupport></uploader-unsupport>
              <uploader-drop >
                <p>上传影像数据</p>
                <uploader-btn  ref="CT"><span>上传CT图像</span></uploader-btn>

                <uploader-btn :directory="true" ref="MRI">上传MRI图像</uploader-btn>
                <uploader-btn :directory="true">上传病理图像</uploader-btn>
                <uploader-btn :directory="true">上传影像报告</uploader-btn>
                <uploader-btn :directory="true">上传病理报告</uploader-btn>
              </uploader-drop>
              <uploader-list></uploader-list>
      </uploader>

  </div>

</template>

<script>

  export default {
    name:'dataUpload',

    data () {
      return {
        dataItem:[
          {
            type:'影像数据',
            flag:'yx'
          },
           {
            type:'病理数据',
            flag:'bl'
          },
           {
            type:'文本数据',
            flag:'wb'
          }
        ],
        options: {

          target: '/api/fileUploader/',
          testChunks: false,
          chunkSize:3*1024*1024,
          single:true
        },
        attrs: {
          accept: 'image/*'
        },
        fileStatusText : {
          success: '上传成功',
          error: '上传失败',
          uploading: '上传中',
          paused: '暂停中',
          waiting: '等待中'
        },
      }
    },
    methods:{


      onFileAdded(file){
        console.log(file)
        // this.computedMD5(file)
      },
      onFileProgress(rootFile, file, chunk) {
        console.log(`上传中 ${file}，chunk：${chunk.startByte / 1024 / 1024} ~ ${chunk.endByte / 1024 / 1024}`)
        console.log(chunk.file)
      },
      onFileSuccess(rootFile, file, response, chunk) {},
      onFileError(rootFile, file, response, chunk) {
          console.log('error')
      },

    },
    mounted(){
      // 1、用原生js获取焦点的方法
      // document.getElementById("myInput").focus()

      // 2、使用vue的方法来获取DOM
      // 先答应下this
      // console.log(this)
      // console.log(this.$refs)
      // var CT=this.$refs.CT
      // this.assignBrowse=this.assign(CT)
      // console.log(this.assignBrowse)
      // this.assignBrowse(this.$refs.MRI)
      // 通过答应this，可以找打$ref下的myInput,所以获取定义的ref可以通过this.$refs.ref的值
      console.log(this.$refs)
      console.log(this.$refs.assignBrowse)
      console.log(this.$refs.assignBrowse.$data)
      // this.$refs.myInput.focus()


    },
  }
</script>

<style>

  .uploader-example {

    width: 700px;
    left: 20%;
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
    display: inline;
  }
  li{
    list-style: none;
  }
</style>
