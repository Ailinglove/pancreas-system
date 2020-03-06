<template>
<div>
<!--  搜索栏-->
  <el-col :span="24" class="wrap-breadcrum">
    	<el-col :span="24" class="toolbar" style="padding-left: 10px;text-align: left">
			<el-form :inline="true" :model="filters">
        <el-form-item style="width: 130px">
          <template>
            <el-select v-model="filters.type" placeholder="请选择">
              <el-option v-for="item in typeData" :key="item.value" :label="item.label" :value="item.value"></el-option>
            </el-select>
          </template>
        </el-form-item>
				<el-form-item style="width: 130px">
					<el-input v-model="filters.name" placeholder="请输入关键字"></el-input>
				</el-form-item>
				<el-form-item>
              <el-button type="primary" @click="getPancreasData">搜索</el-button>
        </el-form-item>
        <el-form-item>
					<el-button type="info" class="el-icon-download" @click="bulkDownload">下载选中数据</el-button>
				</el-form-item>
				<el-form-item>
					<el-button type="primary" class="el-icon-download">全部下载</el-button>
				</el-form-item>
			</el-form>
		</el-col>
  </el-col>


		<el-table :data="tableData.slice((currentPage-1)*pagesize,currentPage*pagesize)"  v-loading="listLoading" highlight-current-row :default-sort = "{prop: 'fields.registerDate', order: 'descending'}" style="width: 90%;">

      <el-table-column type="selection" width="55">
			</el-table-column>
			<el-table-column prop="fields.patientID" label="病人ID" width="150" sortable>
			</el-table-column>
      <el-table-column prop="fields.checkDate" label="扫描时间" width="150" sortable>
			</el-table-column>
      <el-table-column prop="fields.modality" label="模态" width="150" sortable>
			</el-table-column>

			<el-table-column prop="fields.reportResult" label="癌症类型" width="180" sortable>
			</el-table-column>
		</el-table>






    <br>
    <br>
    <div>
       <el-pagination
         style="text-align: left;padding-left: 10px"
        @size-change="handleSizeChange"
        @current-change="handleCurrentChange"
        :current-page="currentPage"
        :page-sizes="[15,20,25]"
        :page-size="100"
        layout="total, sizes, prev, pager, next, jumper"
        :total="tableData.length">
      </el-pagination>
    </div>
   </div>
</template>

<script>
  import {removePancreas,getPancreasList,editPancreas} from '../../api/api'
  import JSZip from 'jszip'
  import FileSaver from 'file-saver'
  import axios from 'axios'
  const getFile = url => {

 return new Promise((resolve, reject) => {

 axios({

  method:'get',

  url,

  responseType: 'arraybuffer'

 }).then(data => {

  resolve(data.data)

 }).catch(error => {

  reject(error.toString())

 })

 })

}
export default {
  data() {
    return {
      data: [ 'api/showDiocm/1.rar', 'api/showDiocm/2.rar'],
      filters: {
        name: '',
        type:1
				},
      typeData:[],


      tableData: [],
      currentPage: 1,
      totalData: 20,
      pagesize:15,
      editFormVisible: false,//编辑界面是否显示
      editLoading: false,
      editFormRules: {
        name: [
          {required: true, message: '请输入姓名', trigger: 'blur'}
        ]
      },
      //编辑界面数据
      editForm: {
        TNM:'',
        tumor_class:''
      },
    }
  },
  methods: {

     bulkDownload(){
          var that = this;
          const zip = new JSZip()
          const cache = {}
          const promises = []
       const data=this.data
          // for(var i =0;i<that.orderAttachment.length;i++){  //循环遍历调用downloadFile方法
          //   const url = that.orderAttachment[i].attachPath;
          //   const iframe = document.createElement("iframe");
          //   iframe.style.display = "none";  // 防止影响页面
          //   iframe.style.height = 0;  // 防止影响页面
          //   iframe.src = url;
          //   document.body.appendChild(iframe);  // 这一行必须，iframe挂在到dom树上才会发请求    // 5分钟之后删除（onload方法对于下载链接不起作用，就先抠脚一下吧）
          //   setTimeout(()=>{
          //     iframe.remove();
          //     }, 5 * 60 * 1000);
          //
          //
          // }
       data.forEach(item => {

  const promise = getFile(item).then(data => { // 下载文件, 并存成ArrayBuffer对象

   const arr_name = item.split("/")

   const file_name = arr_name[arr_name.length - 1] // 获取文件名

   zip.file(file_name, data, { binary: true }) // 逐个添加文件

   cache[file_name] = data

  })

  promises.push(promise)

  })



  Promise.all(promises).then(() => {

  zip.generateAsync({type:"blob"}).then(content => { // 生成二进制流

   FileSaver.saveAs(content, "打包下载.zip") // 利用file-saver保存文件

  })

  })

      },
    getPancreasData() {
			let para = {
					page: this.page,
          type:this.filters.type,
					name: this.filters.name,
          patientID:'',
         searchClick:'0'
				};
				this.listLoading = true;
				  getPancreasList(para).then((res) => {
				    this.tableData=JSON.parse(res.data.data)
					  this.listLoading = false;

				});
			},
    typeInfo(){
      this.typeData=[
        {value:1,label:'模态'},
        {value:2,label:'TNM分期'},
        {value:3,label:'癌症类型'},
      ]
    },






    handleSizeChange(pagesize) {
      this.pagesize = pagesize

    },
    handleCurrentChange(currentPage) {
      this.currentPage = currentPage;

    },
    // 删除病人
    handleDel: function (index, row) {
				this.$confirm('确认删除该记录吗?', '提示', {
					type: 'warning'
				}).then(() => {
					this.listLoading = true;
					//NProgress.start();
					let para = { id: row.pk ,scantime:row.fields.scantime};

					this.$axios.get("/api/pancreas/remove/"+para.id).then(response =>{
					  console.log('数据删除成功')
            this.getPancreasData()
          })
				});
			},
    //点击编辑
    handleEdit(index, row) {
        this.editFormVisible = true;
        this.editForm = Object.assign({}, row); //这句是关键！！！
        console.log(this.editForm)
    },

//点击关闭dialog
    handleClose(done) {
        /*done();
        location.reload();*/
        this.editFormVisible = false;
    },

    //点击取消
    handleCancel(formName) {
        this.editFormVisible = false;
    },

    //点击更新
    handleUpdate(forName) {
      //更新的时候就把弹出来的表单中的数据写到要修改的表格中
      console.log(this.editForm)
      var postData = {
        TNM: this.editForm.TNM,
        tumor_class: this.editForm.tumor_class,
        id: this.editForm.pk

      }
      if (this.editForm.TNM) {
        postData.TNM = this.editForm.TNM
      } else {
        postData.TNM = this.editForm.fields.TNM
      }
      if (this.editForm.tumor_class) {
        postData.tumor_class = this.editForm.tumor_class
      } else {
        postData.tumor_class = this.editForm.fields.tumor_class
      }
      this.$axios.get("/api/pancreas/edit/" + postData.id + '/' + postData.TNM + '/' + postData.tumor_class).then(response => {
        console.log('数据修改成功')
        this.getPancreasData()
      })


      //这里再向后台发个post请求重新渲染表格数据
      this.editFormVisible = false;


    },
  },
   created() {
      this.getPancreasData();
      this.typeInfo()//分类初始化
  },}

</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style>
  .demo-table-expand {
    font-size: 0;
  }
  .demo-table-expand label {
    width: 90px;
    color: #99a9bf;
    font-size: 14px;
    line-height: 20px;
  }
  .demo-table-expand {
    margin-right: 100px
  ;
    margin-bottom: 0;
    width: 100%;
  }
  .el-table td, .el-table th{
    padding: 1px;
  }
  .el-divider{
    font-weight: bold;
  }
  .el-form-item__content {
    line-height: 20px;
    position: relative;
    font-size: 14px;
}

</style>
