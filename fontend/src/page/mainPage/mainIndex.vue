<template>
  <div>
    <el-container>
      <el-header>
        <el-row>
          <el-col :span="2"><div><img src="./imgs/logo.jpg" alt="" style="width: 55px;height: 55px; position: absolute;top:5px;left:0;z-index: 9999;"></div></el-col>
          <el-col :span="20"><h1 style="position: absolute; left: 40%;">医疗大数据智能管理平台</h1></el-col>
           <el-col :span="4" class="login">
              <nav style="position:absolute; right: 3%;">
                  <a href="">注册</a> |
                  <router-link :to="{name:'login'}">登陆</router-link>
              </nav>

           </el-col>
        </el-row>
      </el-header>
      <el-main>
        <div class="mainInfo">
					<ul>
						<li>
							<div style="position:relative;top:50px;padding: 20px">
								<span style="font-size: 30px;">介绍</span>
								<br><br>
								丰富的病种分类、多样的数据格式、精准的数据标注
							</div></li>

					</ul>
				</div>
				<hr color="#808080">
				<div class="item" >
					<ul style="margin-top: 40px;">
            <li v-for="data in tumorType">
              <router-link :to="{name:data.linkPath}">
                <img :src="data.img" :alt="data.type">
                <br>
              <br>
              <span class="tumorType">{{data.type}}</span>
              </router-link>
            </li>
<!--            <li><router-link :to="{name:'数据采集'}"><img src="./imgs/pancre.png" alt="胰腺癌"><br>胰腺癌</router-link></li>-->
<!--						<li><router-link :to="{name:'数据采集'}"><img src="./imgs/glioma.png" alt="脑胶质瘤"><br>脑胶质瘤</router-link></li>-->
<!--						<li><router-link :to="{name:'数据采集'}"><img src="./imgs/eye.png" alt="糖网病"><br>糖网病</router-link></li>-->
<!--						<li><img src="./imgs/2.jpg" alt=""><br>了</li>-->
					</ul>

				</div>

				<hr color="#808080">

				<div class="item" >
					<ul  style="margin-top: 40px;">
						<li v-for="server in serverType">
              <img src="./imgs/server.png" alt="平台服务"><br>{{server}}</li>

					</ul>

				</div>



				<div class="footer" style="color: white;">
					<ul>
						<li>Copyright fudan university all rights reserved 版权所有:复旦大学</li>
					</ul>
				</div>

      </el-main>

    </el-container>
  </div>
</template>

<script>
    export default {
        name: "mainIndex",
      data(){
          return{
            tumorType:[{type:'脑胶质瘤',linkPath:'',img:require('./imgs/glioma.png')},
              {type:'心脑血管疾病',linkPath:'',img:require('./imgs/heartBrain.png')},
              {type:'致盲性眼病',linkPath:'',img:require('./imgs/eye.png')},
              {type:'乳腺肿瘤',linkPath:'',img:require('./imgs/breast.png')},
              {type:'肺癌',linkPath:'',img:require('./imgs/lung.jpg')},
              {type:'肝癌',linkPath:'',img:require('./imgs/liver.jpg')},
              {type:'胰腺肿瘤',linkPath:'数据采集',img:require('./imgs/pancre.png')}
              ,{type:'胃肠肿瘤',linkPath:'',img:require('./imgs/2.jpg')}],
            serverType:['平台服务1','平台服务2','平台服务3','平台服务4']
          }
      }
    }
</script>

<style scoped>
  .el-header {
    background-color: white;
    color: #333;
    line-height: 75px;
  }
  .el-main {
   position:absolute;left:0;top:70px;width:100%;background:#6BA2D6; text-align: center;
  }
  *{margin: 0;}
  .header{position: fixed;z-index:9999;left:0;top:0;height: 90px;background-color: darkorange;color:black;width: 100%;
  font-size:25px;text-align: center;line-height: 60px;}
  .item{position:relative;width: 100%;margin: 20px 0 20px 0;}
  .item li{display: inline-block;width: 300px;height: 300px; margin: 10px;background-color: #ffffff;
    border-radius: 15px;
    padding-top: 30px;}
  .item li:hover{background-color: #B3C0D1;border-radius: 25px;box-shadow: #000000;}
  .mainInfo li{display: inline-block;color: black;text-align: left;
  height: 450px; background-image: url(./imgs/bg.png);background-size: 100% 100%;width: 84%;position: relative;margin: 50px 0 50px 0;text-align: left;}

  .footer li,.mainInfo li,.login li{list-style: none;}
  .login li{display: inline-block;line-height: 30px;margin-left: 10px;padding-left: 10px;
    position: absolute;
    right: 20%;
    height:30px;
    }
  img{margin: 4px;width: 200px;height: 200px;}

/*  注册登陆按钮*/
  a{text-decoration: none;color: black;cursor: pointer}
  .tumorType{
    font-size:1.25rem
  }


</style>
