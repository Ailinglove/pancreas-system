<template>
  <div :class="className" :style="{height:height,width:width}" />
</template>

<script>
import echarts from 'echarts'
require('echarts/theme/macarons') // echarts theme
import resize from './mixins/resize'


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
          data: ['导管腺癌', '神经内分泌肿瘤', '实性假乳头状肿瘤', '浆液性囊腺瘤', '粘液性囊腺瘤']
        },
        series: [
          {
            name: 'WEEKLY WRITE ARTICLES',
            type: 'pie',
            roseType: 'radius',
            radius: [15, 95],//内圈和外圈的半径
            center: ['50%', '38%'],
            data: [
              { value: 320, name: '导管腺癌' },
              { value: 240, name: '神经内分泌肿瘤' },
              { value: 149, name: '实性假乳头状肿瘤' },
              { value: 100, name: '浆液性囊腺瘤' },
              { value: 59, name: '粘液性囊腺瘤' }
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
