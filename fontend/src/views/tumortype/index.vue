<template>
    <div>
      <div class="tumor-type-header" >
        <ul>
          <li @click="turnTo('/home')">首页</li>
          <li :class="{active:active===data.url}" v-for="data in tumorType" @click="turnTo(data.url)">{{data.value}}</li>
        </ul>
      </div>

      <router-view>
      </router-view>

    </div>
</template>

<script>
    export default {
        name: "index",
      data(){
          return {
            tumorType:[
              {index:0,value:'胰腺癌',url:'pancreas'},
              {index:1,value:'乳腺癌',url:'breast'},
              {index:2,value:'肺癌',url:'lung'},
              {index:3,value:'肝癌',url:'liver'},
              {index:4,value:'其他',url:'other'}
            ],
            active:'pancreas'
          }
      },
      methods:{
          turnTo(url){
            if(url==='/home'){
              this.$router.push(url)

            }else{
              this.$router.push('/tumortype/'+url)
            }



          }
      }
    }
</script>

<style scoped>

  .tumor-type-header{
    background: lightsteelblue;
    height: 40px;
    line-height: 40px;
  }

  ul{
    list-style: none;


  }

  li{
    display: inline-block;
    width: 100px;
    text-align: right;
    padding-right: 10px;
    height: 40px;
    line-height: 40px;

    cursor: pointer;

    border-right: 1px solid #ccc;
  }
  li:hover{
    background: skyblue;
  }

  .active{
    background: skyblue;
  }

</style>
