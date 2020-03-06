<template>
    <div>
      <el-card>
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
            title:{text:'胰腺数据分类',x:'center'},
              tooltip : {
                  trigger: 'axis',
                  axisPointer : {            // 坐标轴指示器，坐标轴触发有效
                      type : 'line'        // 默认为直线，可选为：'line' | 'shadow'
                  }
              },
              legend: {
              top:"30",

                  data:['导管腺癌', '神经内分泌肿瘤', '实性假乳头状肿瘤', '浆液性囊腺瘤', '粘液性囊腺瘤']
              },
              grid: {
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
                      name:'导管腺癌',
                      type:'bar',
                      stack:'男',
                      data:[11, 12, 11, 14, 10, 10, 20,20,10,7]
                  },
                  {
                      name:'神经内分泌肿瘤',
                      type:'bar',
                      stack: '男',
                      data:[12, 13, 11, 13, 9, 23, 21,2,2,1]
                  },
                  {
                      name:'实性假乳头状肿瘤',
                      type:'bar',
                      stack: '男',
                      data:[2, 12, 11, 4, 20, 30, 1,1,2,1]
                  },
                  {
                      name:'浆液性囊腺瘤',
                      type:'bar',
                      stack: '男',
                      data:[1, 12, 21, 14, 10, 30, 40,2,2,10]
                  },
                  {
                      name:'粘液性囊腺瘤',
                      type:'bar',
                    stack:'男',
                      data:[2, 18, 4, 16, 19, 16, 10,12,12,10],

                  },
                {
                      name:'导管腺癌',
                      type:'bar',
                      stack:'女',
                      data:[0, 2, 11, 14, 3, 3, 2,20,30,10,2,2,10]
                  },
                  {
                      name:'神经内分泌肿瘤',
                      type:'bar',
                      stack: '女',
                      data:[10, 12, 11, 14, 9, 20, 10,2,2,10]
                  },
                  {
                      name:'实性假乳头状肿瘤',
                      type:'bar',
                      stack: '女',
                      data:[0, 12, 11, 24, 20, 30, 10,2,2,1]
                  },
                  {
                      name:'浆液性囊腺瘤',
                      type:'bar',
                      stack: '女',
                      data:[10, 2, 21, 14, 10, 30, 10,2,1,0]
                  },
                  {
                      name:'粘液性囊腺瘤',
                      type:'bar',
                    stack:'女',
                      data:[2, 18, 4, 16, 19, 16, 10,1,1,10],

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
              title:{text:'胰腺数据分类',x:'center'},
              tooltip:{trigger:'item',
              formatter: "{a} <br/>{b} : {c} ({d}%)"},
              legend:{orient:'vertical',left:'right',
                      data:['胰腺导管腺癌','胰腺神经内分泌肿瘤', '实性假乳头状肿瘤','浆液性囊腺瘤','粘液性囊腺瘤','胰腺导管内乳头状肿瘤']},
              series:[{
                name:'数据分布',
                type:'pie',
                radius:'55%',
                center:['50%','60%'],
                data:[{ value: 33, name: '胰腺导管腺癌' },
              { value: 23, name: '胰腺神经内分泌肿瘤' },
              { value: 19, name: '实性假乳头状肿瘤' },
              { value: 12, name: '浆液性囊腺瘤' },
              { value: 20, name: '粘液性囊腺瘤' },
                { value: 10, name: '胰腺导管内乳头状状瘤' },
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
        min-height: 500px;
        clear: both;
        box-sizing: border-box;
        margin: 0 auto;
    }
  #mychart1 {
        width: 90%;
        min-height: 400px;
        clear: both;
        box-sizing: border-box;
        margin: 0 auto;
    }

</style>
