<template>
    <div>
      <el-card style="height: 500px;">
        <div id="mychart"></div>
      </el-card>
      <el-card>
        <div id="mychart1"></div>
      </el-card>
    </div>
</template>

<script>
    export default {
      name: "DiseaseSpecies",
      mounted() {
          this.draw();
          this.draw1();// 绘制带有性别年龄的图
      },
      methods:{
        draw1(){
          let mychart1=this.$echarts.init(document.getElementById("mychart1"));
          var option={
            title:{text:'胰腺数据模态分布',x:'center'},
              tooltip : {
                  trigger: 'axis',
                  axisPointer : {            // 坐标轴指示器，坐标轴触发有效
                      type : 'shadow'        // 默认为直线，可选为：'line' | 'shadow'
                  }
              },
              legend: {
              top:"30",

                  data:['CT', 'MR','男','女']
              },
              grid: {
                  top:'20%',
                  left: '3%',
                  right: '4%',
                  bottom: '3%',
                  containLabel: true
              },
              xAxis : [
                  {
                      type : 'category',
                      data : [ '10岁以下', '11-20岁', '21-30岁', '31-40岁', '41-50岁','51-60岁', '61-70岁', '71-80岁', '81-90岁','91-100岁']
                  }
              ],
              yAxis : [
                  {
                      type : 'value'
                  }
              ],
              series : [
                  {
                      name:'CT',
                      type:'bar',
                      stack:'img',
                      data:[30, 32, 31, 34, 30, 30, 20,20,30,10]
                  },
                  {
                      name:'MR',
                      type:'bar',
                      stack: 'img',
                      data:[12, 12, 11, 34, 90, 20, 20,12,12,10]
                  },
                  {
                      label:{normal:{show:true}},
                      name:'男',
                      type:'line',
                      data:[20, 12, 11, 24, 20, 30, 10,12,12,10]
                  },
                  {
                    label:{normal:{show:true}},
                      name:'女',
                      type:'line',
                      data:[10, 22, 21, 14, 10, 30, 40,12,12,10]
                  },
              ],

          };
           mychart1.setOption(option)
        },
        draw(){
            //实例化echarts对象
            let mychart=this.$echarts.init(document.getElementById("mychart"));
            //绘制饼图
            var option={
              title:{text:'胰腺数据各模态分布情况',x:'center'},
              tooltip:{trigger:'item',
              formatter: "{a} <br/>{b} : {c} ({d}%)"},
              legend:{orient:'vertical',left:'right',
                      data:['CT','MR', '病理','其它']},
              series:[{
                name:'数据分布',
                type:'pie',
                radius:'55%',
                center:['50%','60%'],
                data:[{ value: 32, name: 'CT' },
              { value: 23, name: 'MR' },
              { value: 10, name: '病理' },
              { value: 3, name: '其它' },


             ]
              }],
              itemStyle: {
                emphasis: {
                    shadowBlur: 10,
                    shadowOffsetX: 0,
                    shadowColor: 'rgba(0, 0, 0, 0.5)'
                }
            }
            };
            mychart.setOption(option)
          }
      }
    }
</script>

<style scoped>
  .el-card{
    margin: 0 auto;
    width: 80%;
    height: 700px;
    margin-bottom: 10px;
  }
  #mychart {
        width: 90%;
        min-height: 400px;
        clear: both;
        box-sizing: border-box;
        margin: 0 auto;
    }
  #mychart1 {
        width: 90%;
        min-height: 500px;
        clear: both;
        box-sizing: border-box;
        margin: 0 auto;
    }

</style>
