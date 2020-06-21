<template>
  <div id="dataInfo">
    <div class="left">

      <case-data></case-data>
    </div>
    <div class="right">
      <segmentation></segmentation>
    </div>

  </div>

</template>

<script>
  import CaseData from "./casedata"
  import segmentation from "../../expend/AICompute/analysis/segmentation";
    export default {
        name: "index",
      components:{
          CaseData,
        segmentation
      },
      methods:{

      }
    }
</script>

<style scoped>
  #dataInfo{
    position: relative;
    display: flex;
    height: 90vh;
    white-space: nowrap;
    top: 20px;
  }
  .left{
    width:40%;
    top: 300px;
    padding: 20px 50px;
    border: #999999 1px solid;

  }

  .right{

    top: 300px;
    width:50%;
    border: #999999 10px solid;
    height: 90%;

  }
</style>
