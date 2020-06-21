<template>
  <div class="mainindex">
    <h1 class="title">智能样本数据集汇总</h1>
    <div class="mainbox">
      <div class="box">
        样本集
            <div class="sampleList" style="">
              <ul>
                <li class="sample" v-for="sample in sampleData">
                  <span class="type" style="">{{sample.type}} </span>: {{sample.totalNum}}

                </li>
              </ul>
            </div>
      </div>
      <div class="box">
        访问量
        <div >  <div class="sampleList">
          <ul>
            <li class="sample" v-for="sample in visitedData">
              <span class="type" style="">{{sample.type}} </span>: {{sample.totalNum}}

            </li>
          </ul>
        </div></div>
        <div>
          资源使用率
          <div class="sampleList">
            <ul>
              <li class="sample" v-for="sample in systemSourceData">
                <span class="type" style="">{{sample.type}} </span>: {{sample.totalNum}}

              </li>
            </ul>
          </div>
        </div>

      </div>
    </div>
  </div>

</template>

<script>
  export default {
    name: "index",
    data(){
      return {
        sampleData:[{type:'脑胶质瘤',totalNum:220},
          {type:'心脑血管疾病',totalNum:2120},
          {type:'致盲性眼病',totalNum:2220},
          {type:'乳腺瘤',totalNum:330},
          {type:'肝癌',totalNum:2220},
          {type:'胰腺肿瘤',totalNum:5320},
          {type:'肠胃肿瘤',totalNum:1290}],
        visitedData:[{type:'今日访问量',totalNum:2220},
          {type:'访问总量',totalNum:2220} ],
        systemSourceData:[
          {type:'CPU利用率',totalNum:'30%'},
          {type:'网络占用率',totalNum:'40%'},
          {type:'硬盘占用率',totalNum:'8%'},
        ]
      }
      }

  }

</script>

<style scoped>
  .sampleList{
    padding-top: 20px;
  }
  .mainindex{
    /*background: url("../../../static/bg4.jpg") no-repeat;*/
    background-size: 100% 100%;
    height: 100%;
    overflow: hidden;
    color: white;

  }
  .title{
    color: white;
    margin-top: 20px;
  }
  .mainbox{
    height: 90%;
    width: 60%;

    margin: 0 auto;
    top:100px;
    display: flex;
    align-items: center;
    text-align: center;
  }
  .box{
    width: 100%;
    height: 80%;
    float: left;
    border: #2c3e50 5px solid;
    padding-top: 50px;

  }
  .sample{
    position: relative;


    list-style: none;
    text-align: left;

  }
  .type{
    margin-bottom: 20px;
    display: inline-block;
    width: 100px;
    font-size: 14px;
    color: #156798;



  }

</style>
