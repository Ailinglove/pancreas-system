<template>
<!--    一个病人的所有数据-->
  <div >
    <a href="http://localhost:8080/#/userlist" class="el-icon-back">病人中心</a>



    <div style="position: relative;top: 30px;width: 100%">
         <el-card>
      <div slot="header" class="clearfix">
        <el-button type="success" plain @click="jump('basicinfo')">基本信息</el-button>
      </div>
        <el-form  inline label-width="100px" size="mini">
          <el-table :data="detailData.basciInfo"  highlight-current-row style="width: 100%;">
            <el-table-column prop="fields.casename" label="姓名"  width="400">
            </el-table-column>
             <el-table-column prop="fields.sex" label="性别"  >
            </el-table-column>
             <el-table-column prop="fields.age" label="年龄"  >
            </el-table-column>
            <el-table-column prop="fields.patientID" label="患者ID号" >
            </el-table-column>
            <el-table-column prop="fields.houspitalID" label="住院号"  >
            </el-table-column>
            <el-table-column prop="fields.smoking" label="吸烟喝酒" >
            </el-table-column>
            <el-table-column prop="fields.GeneticH" label="遗传史"  >
            </el-table-column>
            <el-table-column prop="fields.GeneticH"  >
            </el-table-column>
          </el-table>
        </el-form>
    </el-card>

          <el-card>
      <div slot="header" class="clearfix">
        <el-button type="success" plain @click="jump('imginfo')">影像信息</el-button>
<!--        <el-button style="float: right;padding: 3px 0;" type="text">操作按钮</el-button>-->
      </div>

        <el-form  label-width="100px" size="mini" style="text-align:right">
          <el-table :data="detailData.imgInfo"  highlight-current-row style="width: 100%;">

            <el-table-column prop="fields.houspitalID" label="住院号"  >
            </el-table-column>
            <el-table-column prop="fields.modality" label="模态"  >
            </el-table-column>
            <el-table-column prop="fields.checkDate" label="扫描时间" >
            </el-table-column>
             <el-table-column prop="fields.checkMethod" label="检查方法" >
            </el-table-column>
            <el-table-column prop="fields.checkDevice" label="扫描设备" >
            </el-table-column>

            <el-table-column prop="fields.imgReport" label="影像报告" width="400" >
            </el-table-column>
             <el-table-column label="操作" >
              <template >
                <el-button type="success" size="small" @click="showDicom(index.row)">显示</el-button>
              </template>
            </el-table-column>
          </el-table>
        </el-form>

    </el-card>
          <el-card>
      <div slot="header" class="clearfix">
        <el-button type="success" plain @click="jump('pathoinfo')">病理信息</el-button>

      </div>

        <el-form  label-width="100px" size="mini" style="text-align:left">
         <el-table :data="detailData.pathoInfo"  highlight-current-row style="width: 100%;">
            <el-table-column prop="fields.pathoID" label="病理号"  >
            </el-table-column>
            <el-table-column prop="fields.pathoReport" label="病理报告" width="400" >
            </el-table-column>
            <el-table-column prop="fields.tumorClass" label="肿瘤类型" >
            </el-table-column>
           <el-table-column prop="fields.TNM" label="TNM分期">
            </el-table-column>
            <el-table-column prop="fields.differentiation" label="分化程度">
            </el-table-column>
           <el-table-column prop="fields.size" label="肿瘤大小">
            </el-table-column>
           <el-table-column label="操作" width="150">
				<template >
          <el-button type="success" size="small" @click="handleEdit(index,row)">编辑</el-button>
				</template>
			</el-table-column>
          </el-table>
        </el-form>

    </el-card>
    </div>


  </div>
</template>

<script>
  import {getPatientList,getPancreasList,getPathoInfoList} from '../../../../src/api/api'
    export default {
      name: "detailInfo",
      data(){
          return {
            dividerData:['基本信息','影像数据','病理数据','基因数据'],
            ID:'G03748360',
            houspitalID:'',
            detailData:{
              basciInfo:[],
              imgInfo:[],
              pathoInfo:[],
              geneInfo:[],
            }

          }
      },
      created() {
         this.ID=this.$route.params.patientID;
        this.houspitalID=this.$route.params.houspitalID;
        console.log(this.houspitalID,this.$route.params.houspitalID)

        this.getBasicInfo();
        this.getImgInfo();
        this.getPathoInfo();

    //
    },

      methods:{

        showDicom(index,row){
          var data = Object.assign({}, row); //这句是关键！！！
          window.alert('显示'+data.fields.patientID+' 的影像数据')

        },
        jump(type){
          if(type==='basicinfo'){

            this.$router.push({path: '/userlist'})
          }else if(type==='imginfo'){

            this.$router.push({path: '/YXDataManagement'})

          }else if(type==='pathoinfo'){

            this.$router.push({path: '/BLDataManagement'})

          }

  },



        getBasicInfo(){
          console.log(this.$route.path)
          let param={
            patientID:this.$route.params.patientID,
            houspitalID: this.$route.params.houspitalID
          }

          getPatientList(param).then((res)=>{
            this.detailData.basciInfo=JSON.parse(res.data.data)
             this.detailData.basciInfo = this.unique( this.detailData.basciInfo);

          });
        },
        getImgInfo(){
          let param={
            patientID:this.ID,
            houspitalID: this.houspitalID
          }
          if (this.houspitalID===''){
            this.detailData.imgInfo=""
          }

          else{getPancreasList(param).then((res)=>{

            this.detailData.imgInfo=JSON.parse(res.data.data)

          });}
        },
        unique(arr) {
        const res = new Map();
        return arr.filter((arr) => !res.has(arr.fields.patientID) && res.set(arr.fields.patientID, 1));
      },
        getPathoInfo(){
          let param={
            patientID:this.ID,
            houspitalID: this.houspitalID
          }
          if (this.houspitalID===""){
            this.detailData.imgInfo=""
            window.alert('现有数据库中还没有该病人的数据报告')
          }
          else{
            getPathoInfoList(param).then((res)=>{
            this.detailData.pathoInfo=JSON.parse(res.data.data)

          });
          }

        },
        getGeneInfo(){
          let param={
            patientID:this.ID,
            houspitalID: this.houspitalID
          }
          getPatientList(param).then((res)=>{
            this.detailData.geneInfo=JSON.parse(res.data.data)

          });


        }
      },

    }
</script>

<style slot>

  .el-card{
    width:90%;

    position: relative;
    margin: 0 auto;
    margin-bottom: 10px;



  }
.text {
    font-size: 14px;
  }

  .item {
    margin-bottom: 10px;
    margin-left: 10px;
    text-align: left;
    border-bottom: 1px solid #ededed;
  }
  .info{
    width: 50%;
     ;
    position: absolute;
    left: 150px;
  }
  .clearfix:before,
  .clearfix:after {
    display: table;
    content: "";
  }
  .clearfix:after {
    clear: both
  }

  .box-card {
    width: 480px;
  }
  .detailDiv{
    width:80%;
    margin-left: auto;
    margin-right: auto;
    margin-top: 3px;
  }
  a{
    text-decoration: none;
    color: #777777;
    font-size: 18px;
    position: absolute;
    left: 90px;
    top: 30px;

  }

</style>
