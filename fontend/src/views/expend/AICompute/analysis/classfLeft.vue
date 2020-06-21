<template>
  <div class="left">

    <dragImg></dragImg>
  </div>
</template>

<script>
  import dragImg from "./dragImg";
  export default {
    components:{
      dragImg
    },
    name: "classfLeft"
  }
</script>

<style scoped>
  .left{
    width: 500px;
    height: 500px;
    border: gray 1px dashed;
    color: gray;

  }
  /*span{*/
  /*  position: relative;*/
  /*  line-height: 400px;*/
  /*}*/
</style>
