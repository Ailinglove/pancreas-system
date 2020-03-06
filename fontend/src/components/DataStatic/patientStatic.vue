<template>
  <div>
    <el-card>
      <div id="myChart"></div>
    </el-card>
  </div>




</template>

<script>
    export default {
        mounted () {
            // 调用绘制图表的方法
            this.draw();
        },
        methods: {
            draw () {
                // 实例化echarts对象
                let myChartDrawer = this.$echarts.init(document.getElementById('myChart'))

                // 绘制条形图
                var option = {
                    tooltip:{trigger:'axis',axisPointerL:{type:'line'}},
                    title: {
                        text: '按照病人进行统计分布',
                        top: 5,
                        left: 'center'
                    },
                    legend: {
                        data: ['男', '女','各年龄段总人数'],
                        top: 40
                    },
                  grid:{
                      top:'30%'
                  },
                    // X轴
                    xAxis: {
                         data : [ '10岁以下', '11-20岁', '21-30岁', '31-40岁', '41-50岁','51-60岁', '61-70岁', '71-80岁', '81-90岁','91-100岁']

                    },
                    // Y轴
                    yAxis: {
                      display:true
                    },
                    // 数据
                    series: [
                        {
                          label:{normal:{show:true}},
                          name: '男',
                          type: 'bar',
                          data: [0, 2, 3, 8, 6,12, 12, 23, 10, 10]
                        },
                        {
                          label:{normal:{show:true}},
                          name: '女',
                          type: 'bar',
                          data: [1, 1, 5, 4, 10,20, 10, 20, 30, 10]
                        },
                      {
                        label: {normal: {show: true}},
                        name: '各年龄段总人数',
                        type: 'line',
                        data: [1, 3, 8, 12, 16, 22,22, 43, 40, 20]
                      }
                    ]
                };

                myChartDrawer.setOption(option);
            }
        }
    }
</script>

<style scoped>
  .el-card{
    margin: 0 auto;
    width: 80%;
    height: 400px;
    top:20px;
    position:relative;
  }
    #myChart {
        width: 90%;
        min-height: 400px;
        clear: both;
        box-sizing: border-box;
        margin: 0 auto;
    }
</style>
