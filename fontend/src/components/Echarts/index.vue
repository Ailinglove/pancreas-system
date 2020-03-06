<template>
  <div class="chart-container" >
    <span style="text-align: center">数据分布可视化</span>
    <br>
    <div style="position: absolute;top: 100px ! important">
       <chart height="400px" width="100%" />
    <hr/>
      <PieChart class="inline-block" height="400px" width="600px"/>
      <BarChart class="inline-block" height="400px" width="600px"/>
    </div>

    <div>

    </div>
  </div>
</template>

<script>
import Chart from '@/components/Echarts/Charts/lineMarker'
import PieChart from '@/components/Echarts/Charts/PieChart'
import BarChart from '@/components/Echarts/Charts/BarChart'

export default {
  name: 'indexLine',
  components:
    { Chart,
      PieChart,
      BarChart

  }

}
</script>

<style scoped>
  .chart-container{
    overflow:auto !important;
    background-color: #ffffff;
  position: absolute;
    width: 100%;
    height: 100%;
    text-align: center;
  }
  .inline-block{
    float: left;
  }


</style>

