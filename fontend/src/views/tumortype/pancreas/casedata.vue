<template>

    <div >
      数据情况
      <button class="option" @click="startAnalysis">开始分析</button>
      <button class="option">诊断结果</button>
      <el-table :data="data" style="width: 100%;" height="700"
                ref="multipleTable"
                @selection-change="handleSelectionChange"
      >
        <el-table-column
          type="selection"
          width="55">
        </el-table-column>
        <el-table-column label="姓名" prop="fields.casename" width="140" > </el-table-column>
        <el-table-column label="年龄" prop="fields.age" > </el-table-column>
        <el-table-column label="性别" prop="fields.sex" > </el-table-column>
        <el-table-column label="分类结果" prop="fields.classres" > </el-table-column>
        <el-table-column label="分割结果" prop="fields.segres" > </el-table-column>

        <el-table-column prop="fields.status" label="状态"
        >
          <template scope="scope" >
            <div class="status" >
              <div :class="{'active':scope.row.fields.status==1}">
              </div>
            </div>
          </template>
        </el-table-column>
        <el-table-column label="操作" width="220" >
          <template scope="scope" >
            <div  >
              <el-button  size="small" type="success" @click="showDicom()" :disabled="!Boolean(scope.row.fields.status==1)">查看</el-button>

            </div>
          </template>
        </el-table-column>
      </el-table>
      <el-button @click="toggleSelection()">取消选择</el-button>
      <el-button @click="pause()">{{status[type].value}}</el-button>


      <div style="text-align: left">
        <p>一共分析：{{totalAnalysisNum}}个病例</p>
        <p>已经分析：{{analysisNum}}个病例</p>
        <p>平均耗时：{{averageDate | getAve()}}分钟</p>


        <p>开始时间：{{startDate | formatTime}} </p>
        <p>结束时间：{{endDate | formatTime}} </p>
        <p>共计用间：{{endDate-startDate| getAve()}}分钟 </p>
        <el-progress  :text-inside="true" :stroke-width="24" :percentage="percentage" status="success"></el-progress>
        <p>预计剩余时间 {{averageDate*(totalAnalysisNum-analysisNum) | getAve()}}分钟 </p>
      </div>
    </div>




</template>

<script>
  import caseItem from "./caseItem";
  import segment from "@/views/expend/AICompute/analysis/segmentation"
  var timer=0
  Date.prototype.format = function(fmt) {
    var o = {
      "M+" : this.getMonth()+1,                 //月份
      "d+" : this.getDate(),                    //日
      "h+" : this.getHours(),                   //小时
      "m+" : this.getMinutes(),                 //分
      "s+" : this.getSeconds(),                 //秒
      "q+" : Math.floor((this.getMonth()+3)/3), //季度
      "S"  : this.getMilliseconds()             //毫秒
    };
    if(/(y+)/.test(fmt)) {
      fmt=fmt.replace(RegExp.$1, (this.getFullYear()+"").substr(4 - RegExp.$1.length));
    }
    for(var k in o) {
      if(new RegExp("("+ k +")").test(fmt)){
        fmt = fmt.replace(RegExp.$1, (RegExp.$1.length==1) ? (o[k]) : (("00"+ o[k]).substr((""+ o[k]).length)));
      }
    }
    return fmt;
  }
    export default {
        name: "CaseData",
      components:{
          caseItem,
        segment
      },
      computed:{
          setEndDate:{
            get(){
              return this.endDate
            },
            set(newDate){
              this.endDate=newDate
              return newDate
            }
          }
      },
      data(){
          return{
            tableTitle:[],
            data:[],
            selectedData:[],
            totalAnalysisNum:0,
            analysisNum:0,
            startDate:new Date(),
            endDate:new Date(),
            averageDate:0,
            percentage:0,
            pausebtn:false,
            currentIndex:0,
            type:0,
            status:[{type:0,value:'暂停'},{type:1,value:'继续'}]


          }
      },
      filters: {
        getAve(time) {
          return (time / 3600).toFixed(2)
        },
        formatTime(date) {

          return date.format("yyyy-MM-dd hh:mm:ss")

        },
      },
        mounted() {
          this.$axios.get("api/pancrease/", {}).then(res => {
            // console.log(JSON.parse(res.data.data));
            this.data = JSON.parse(res.data.data)
            console.log(this.data)
          });
        },
        methods: {
          processData(){
            return new Promise(((resolve, reject) => {
              setTimeout(()=>{
                console.log('正在处理')
                resolve()
              },3000)
              })
            )


          },

          startAnalysis() {
            this.startDate = new Date()

            for (let i=0; i < this.selectedData.length; i++) {

                timer=setTimeout(() => {
                  this.currentIndex++
                  if(this.pausebtn){
                    window.clearTimeout(timer)

                  }else{

                    console.log(i,this)
                    this.selectedData[i].fields.status = 1
                    this.selectedData[i].fields.classres = '类别' + i
                    this.analysisNum++
                    this.setEndDate = new Date()

                    this.averageDate = (this.endDate - this.startDate) / this.analysisNum
                    this.percentage = Number(((this.analysisNum / this.totalAnalysisNum) * 100).toFixed(2))

                }
              }, 1000 * i, i)
            }

          },
          pause(){
            this.type=1-this.type
            this.pausebtn=true
          },
          toggleSelection(rows) {

            if (rows) {
              rows.forEach(row => {
                this.$refs.multipleTable.toggleRowSelection(row);
              });
            } else {
              this.$refs.multipleTable.clearSelection();
            }
            this.selectedData = rows
          },
          handleSelectionChange(val) {
            this.selectedData = val
            this.multipleSelection = val;
            this.totalAnalysisNum = val.length
            console.log('选中', this.selectedData)
          },

          gender(value) {
            if (value === 0) {
              return '女'
            } else {
              return '男'
            }
          },
          showDicom() {

          },
          created() {
            this.data.map(item => {
              item.gender = this.gender(item.gender)
            })
          }
        }
      }


</script>

<style scoped>
  .container{
    display: flex;
  }
  .left{
    width: 50%;
  }
  .right{
    width: 50%;
    border: 1px springgreen solid;
  }
  .status{
    width: 30px;height: 30px;
    border-radius: 50%;
    background: #999999;
    color: red;

  }
  .active{
    width: 30px;height: 30px;
    border-radius: 50%;
    background: green;

  }
  .option{
    background: skyblue;
    border: 1px solid gray;
    width: 100px;
    height: 30px;
    border-radius: 20px;
    margin-left: 10px;
  }
</style>
