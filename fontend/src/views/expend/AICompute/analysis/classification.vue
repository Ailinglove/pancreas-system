<template>
  <div style="height: 100%;background-color:rgba(0,0,0,0.7);overflow: auto">
    <div class=" box1" >
      <div style="display: flex;flex-direction: row;flex-wrap: nowrap">
        <div class="rowfunction"><strong>智能数据分析</strong></div>
        <div class="rowfunction" >
            <span>病种选择:</span>
            <select name="type" v-model="selectedData" @change="getSelectedData">
              <option v-for="data in tumorType" :value="data.value">{{data.label}}</option>
            </select>
          </div>
          <div class="rowfunction">
            <span>数据格式:</span>
            <select>
              <option v-for="data in dataType" value="data.value">{{data}}</option>
            </select>
          </div>
        <div class="rowfunction">
          <input type="button" class="btnanalysis" @click="startAnalysis" value="开始分析">
        </div>
      </div>
    </div>
    <div class="main" style="color: floralwhite">
      <div class="box box2" style="flex-grow: 2;margin: 0 2px;">
        <classfLeft style="margin: 0 auto"></classfLeft>
        <img src="./img/loading2.gif" class="loading" style="" v-show="showimg">

      </div>
      <div class="box box3" style="width:500px;">
        <strong>{{title}}</strong>
        <div class="rightbox" style="color: #696A6C">{{rightData}}</div>
        <div class="rightbox" style="text-align: left">
          分类结果：<span style="border-bottom: 1px solid gray">{{result}}</span>
        </div>
      </div>
    </div>
  </div>

</template>

<script>
  import classfLeft from "./classfLeft";
  import dragImg from "./dragImg";
  export default {
    name: "index",
    components:{
      classfLeft,
      dragImg
    },
    data(){
      return {
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
        showimg:false

      }
    },
    methods:{
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
          that.result='AI计算的分类结果'
          console.log('nihao',this.showimg)
        },2000)


      }
    },
    created() {
      this.selectedData=this.tumorType[0].value
      this.rightData=this.tumorDic['yixian']
    }
  }
</script>

<style scoped>
  *{
    box-sizing: content-box;
  }
  .btnanalysis{
    height: 30px;
    border-radius: 10px;
  }
  .btnanalysis:hover{
    background-color: #cccccc;
  }
.main{
  width: 99%;border:1px solid black;
  margin: 0 auto;height: 90%;
  display: flex;
  justify-content: space-around;
}
  .box{
    height: 99%;
    border-right: 1px solid gray;
    border-left: 1px solid gray;

  }
  .box1{
    display: flex;
    align-items: center;

    width: 99%;
    height: 6%;
    margin: 10px auto;
    background-color: #49494a;
  }
  select{
    height: 30px;
    width: 120px;
    font-size: 14px;
    border-radius: 2px;

  }
  .rowfunction{
    margin: 0 10px 0 0 ;
    width: 200px;
  }
  .rightbox{
    text-align: left;
    padding: 20px 30px;color: whitesmoke
  }
  .loading{
    position:fixed;width: 200px;height: 200px;
    top:50%;transform: translate(-50%,-50%);

  }

</style>
