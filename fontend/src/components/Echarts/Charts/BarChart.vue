<template>
  <div id="mybar" :class="className" :style="{height:height,width:width}" />
</template>

<script>
  import echarts from 'echarts'
  import resize from './mixins/resize'
require('echarts/theme/macarons') // echarts theme


export default {
  mixins: [resize],
  props: {//对饼图基本属性的设置
    className: {
      type: String,
      default: 'chart'
    },
    width: {
      type: String,
      default: '100%'
    },
    height: {
      type: String,
      default: '300px'
    }
  },
  data() {
    return {
      chart: null
    }
  },
  mounted() {
    this.$nextTick(() => {
      this.initChart()
    })
  },
  beforeDestroy() {
    if (!this.chart) {
      return
    }
    this.chart.dispose()
    this.chart = null
  },
  methods: {
    initChart() {
      this.chart = echarts.init(this.$el, 'macarons')

      this.chart.setOption({
        tooltip: {
          trigger: 'item',
        },
        legend: {//图例
          left: 'center',
          bottom: '10',
          data: ['CT','MR','其他']
        },
        series: [
          {
            name: 'WEEKLY WRITE ARTICLES',
            type: 'pie',
            roseType: 'radius',
            radius: [15, 95],//内圈和外圈的半径
            center: ['50%', '38%'],
            data: [
              { value: 320, name: 'CT' },
              { value: 240, name: 'MR' },
              { value: 149, name: '其他' },
            ],
            animationEasing: 'cubicInOut',
            animationDuration: 2600
          }
        ]
      })
    }
  }
}
</script>
