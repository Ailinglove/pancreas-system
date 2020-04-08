<template>
  <div id="container" ></div>

</template>
<style scoped>
  #container{
    width:100%;
    height: 700px;
  }
</style>

<script>

  import {AMapManager, lazyAMapApiLoaderInstance} from 'vue-amap'

  let amapManager = new AMapManager()
  export default {
    mounted(){
      var map = new AMap.Map('container', {
        zoom:4,//级别
        center: [116.397428, 39.90923],//中心点坐标

        mapStyle: 'amap://styles/ee67e629cd8190d40a962318a4d31408'
      });
    },
    data () {
      return {
      }
    },




  }



</script>
