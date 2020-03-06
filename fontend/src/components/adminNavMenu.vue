<template>
  <div>
    <div >
          <ul >
          <li v-for="data in dataItem" >
            <div class="uploader-container">
              <uploader :options="options" class="uploader-example">
              <uploader-unsupport></uploader-unsupport>
              <uploader-drop>
                <p>上传{{data.type}}</p>

                <uploader-btn v-if="data.flag=='yx'">单个DCM图像</uploader-btn>
                 <uploader-btn v-else-if="data.flag=='bl'">单个病理图像</uploader-btn>
                 <uploader-btn v-else="ata.flag=='wb'">上传文本数据(临床数据、肿瘤标志物文件、基因数据)</uploader-btn>
          <!--      <uploader-btn :attrs="attrs">select images</uploader-btn>-->
                <uploader-btn v-if="data.flag!='wb'":directory="true">批量上传</uploader-btn>
              </uploader-drop>
              </uploader>
               <uploader-list></uploader-list>
            </div>
            <div class="uploader-container" style="width: 30%;background-color: #ededed">

            </div>


          </li>
    </ul>
    </div>


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
          // https://github.com/simple-uploader/Uploader/tree/develop/samples/Node.js
          target: '/api/ret_pancreasinfolist/',
          testChunks: false
        },
        attrs: {
          accept: 'image/*'
        }
      }
    }
  }
</script>

<style>
  .uploader-container{

  }
  .uploader-example {
    width: 400px;
    padding: 15px;
    margin: 40px 10px 10px 10px;
    font-size: 12px;
    box-shadow: 0 0 10px rgba(0, 0, 0, .4);
  }
  .uploader-example .uploader-btn {
    margin-right: 4px;
  }
  .uploader-example .uploader-list {
    max-height: 200px;
    overflow: auto;
    overflow-x: hidden;
    overflow-y: auto;
  }
  li{
    list-style: none;
    width: 100%;
  }
</style>
