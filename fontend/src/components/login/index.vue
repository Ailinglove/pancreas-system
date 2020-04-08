<template>
  <div>
    <div class="top-content">
      <div class="inner-bg" >
        <div class="container">
            <div class="row">
                <div class="col-sm-8 col-sm-offset-2 text">
                    <h1><strong>胰腺数据管理系统</strong> </h1>
                 </div>
            </div>
            <div class="row">
                <div class="col-sm-6 col-sm-offset-3 form-box">
                  <div class="form-top">
                    <div class="form-top-left">

                        <p>请输入您的账号和密码</p>
                    </div>
                    <div class="form-top-right">
                      <i class="fa fa-lock"></i>
                    </div>
                    </div>
                    <div class="form-bottom">
                  <form @submit.prevent="Loginhandle" role="form" action="" method="post" class="login-form">
                    <div class="form-group">
                      <label class="sr-only" for="form-username">账号</label>
                        <input type="text" name="form-username" placeholder="账号..." class="form-username form-control" id="form-username" v-model="username">
                      </div>
                      <div class="form-group">
                        <label class="sr-only" for="form-password">密码</label>
                        <input type="password" name="form-password" placeholder="密码..." class="form-password form-control" id="form-password" v-model="password">
                      </div>

                      <button type="submit" class="btn" style="width: 100px;" >登陆</button>
                  </form>
                </div>
                </div>
            </div>
        </div>
    </div>

    </div>
  </div>
</template>

<script>
  export default {
    data(){
      return {
        username:'',
        password:''
      }
    },
    methods:{
      Loginhandle(){

        this.$router.push({name:'mainPage'})
        console.log('跳转到主界面')
      }
    }
  }
</script>

<style lang="scss">
  .top-content{
    width: 100%;
    height: 100%;
    max-height: 100%;
    position: absolute;
    z-index: 99999;
    left: 0;
    top: 0;
    background:#8DC3FF;
    background-size: 100% 100%;
  }
  .inner-bg{

    width: 30%;
    height: 50%;
    position: relative;
    top: 20%;
    left: 40%;
    color: white;
    -webkit-border-radius: 10px;
    -moz-border-radius: 10px;
    border-radius: 10px;
  }
  strong { font-weight: 500; }
  h1, h2 {
    margin-top: 10px;
    font-size: 38px;
      font-weight: 100;
      color: white;
      line-height: 50px;
  }
  ::-moz-selection { background: #de615e; color: #fff; text-shadow: none; }
  ::selection { background: #de615e; color: #fff; text-shadow: none; }
  .form-box {
    margin-top: 35px;
  }
  .form-top {
    overflow: hidden;
    padding: 0 25px 15px 25px;
    background: #444;
    background: rgba(0, 0, 0, 0.35);
    -moz-border-radius: 4px 4px 0 0; -webkit-border-radius: 4px 4px 0 0; border-radius: 4px 4px 0 0;
    text-align: left;
  }
  .form-top-left {
    float: left;
    width: 75%;
    padding-top: 25px;
  }

  .form-top-left h3 { margin-top: 0; color: #fff; }
  .form-top-left p { opacity: 0.8; color: #fff; }

  .form-top-right {
    float: left;
    width: 25%;
    padding-top: 5px;
    font-size: 66px;
    color: #fff;
    line-height: 100px;
    text-align: right;
    opacity: 0.3;
  }

  .form-bottom {
    padding: 25px 25px 30px 25px;
    background: #444;
    background: rgba(0, 0, 0, 0.3);
    -moz-border-radius: 0 0 4px 4px; -webkit-border-radius: 0 0 4px 4px; border-radius: 0 0 4px 4px;
    text-align: left;
  }

  .form-bottom form textarea {
    height: 100px;
  }

  .form-bottom form button.btn {
    width: 100%;
  }

  .form-bottom form .input-error {
    border-color: #de615e;
  }
  .form-group{ margin-bottom: 20px;border-radius: 4px;
    font-size: 20px;}
  .form-control{margin-left: 10px; font-size: 20px}
  .btn{border-radius: 4px; margin-top: 10px;}




</style>

