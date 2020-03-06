<template>
<div>
<!--  搜索栏-->
  <el-col :span="24" class="wrap-breadcrum">
    	<el-col :span="24" class="toolbar" style="padding-bottom: 20px;">
			<el-form v-model="searchItem" :inline="true" :model="filters" style="text-align: left;" size="mini" label-position="left" label-width="100px">
 <el-form-item label="姓名:"><el-input v-model="searchItem.casename" label="casename"></el-input></el-form-item>
        <el-form-item label="住院号:"><el-input v-model="searchItem.houspitalID" label="houspital"></el-input></el-form-item>
        <el-form-item label="分化程度：">
          <el-input v-model="searchItem.differentiation" label="houspital"></el-input>

        </el-form-item>
        <el-form-item label="癌症类型：" >
          <el-select  v-model="searchItem.tumorClass" >
            <el-option v-for="item in tumorClass" :key="item.value" :label="item.label" :value="item.value"></el-option>
          </el-select>
        </el-form-item>

        <el-form-item label="TNM分期" style="width: 300px">
          <el-input v-model="searchItem.TNM" ></el-input>
<!--            <el-date-picker v-model="editForm.checkDate" style="width: 180px;"type="date" placeholder="请选择上传日期"></el-date-picker>-->
        </el-form-item>

				<el-form-item style="width: 100px">
              <el-button type="primary" class="el-icon-search" @click="getPathoInfoList">搜索</el-button>

        </el-form-item>
        <el-form-item style="width: 100px">
            <el-button type="primary" class="el-icon-search" @click="getPathoInfoList">全部</el-button>

        </el-form-item>
			</el-form>
		</el-col>
  </el-col>


		<el-table :data="tableData.slice((currentPage-1)*pagesize,currentPage*pagesize)"  v-loading="listLoading" highlight-current-row :default-sort = "{prop: 'fields.registerDate', order: 'descending'}" style="width: 100%;">
		<el-table-column type="expand">
        <template slot-scope="props" >
          <el-form label-position="left" inline  class="demo-table-expand">
            <el-form-item label="病理报告" >
              <span class="item_content">{{props.row.fields.pathoReport}}</span>
            </el-form-item>

          </el-form>

        </template>
      </el-table-column>
			<el-table-column type="index" width="50">
			</el-table-column>
			<el-table-column prop="fields.casename" label="姓名" width="150" sortable>
			</el-table-column>
      <el-table-column prop="fields.houspitalID" label="住院号" width="100" sortable>
			</el-table-column>
			<el-table-column prop="fields.pathoID" label="病理号" width="100" sortable>
			</el-table-column>
			<el-table-column prop="fields.tumorClass" label="肿瘤类型" width="180" sortable>
			</el-table-column>
      <el-table-column prop="fields.size" label="肿瘤大小" width="110" sortable>
			</el-table-column>
      <el-table-column prop="fields.differentiation" label="分化程度" width="110" sortable>
			</el-table-column>
      <el-table-column prop="fields.TNM" label="TNM分期" width="110" sortable>
			</el-table-column>
			<el-table-column label="操作" width="220" >
				<template slot-scope="scope">
<!--					<el-button type="info" size="small" @click="handleShowBingLi(scope.$index, scope.row)">显示</el-button>-->
          <el-button  size="small" type="success" @click="handleEdit(scope.$index, scope.row)">编辑</el-button>

					<el-button type="danger" size="small" @click="handleDel(scope.$index, scope.row)">删除</el-button>
				</template>
			</el-table-column>
		</el-table>


    <el-dialog title="编辑"
     :visible.sync="editFormVisible"
     :close-on-click-modal="false"
     class="edit-form"
     :before-close="handleClose">
      <el-form v-model="editForm" label-width="80px" :rules="editFormRules" ref="editForm">
         <el-form-item label="姓名" prop="fields.casename">
              <el-input v-model="editForm.casename " auto-complete="off"></el-input>
          </el-form-item>
         <el-form-item label="分化程度" prop="fields.differentiation">
              <el-input v-model="editForm.differentiation " auto-complete="off"></el-input>
          </el-form-item>
          <el-form-item label="TNM分期" prop="fields.TNM">
              <el-input v-model="editForm.TNM " auto-complete="off"></el-input>
          </el-form-item>
        <el-form-item label="癌症类型" prop="fields.tumorClass">
              <el-select v-model="editForm.tumorClass" placeholder="请选择">
                <el-option
                  v-for="item in tumorClass"
                  :key="item.value"
                  :label="item.label"
                  :value="item.value">
                </el-option>
            </el-select>
          </el-form-item>
      </el-form>
      <div slot="footer" class="dialog-footer">
          <el-button @click.native="handleCancel('editForm')">取消</el-button>
          <el-button type="primary" @click.native="handleUpdate('editForm')">更新</el-button>
      </div>
    </el-dialog>



    <br>
    <br>
    <div>
       <el-pagination
        @size-change="handleSizeChange"
        @current-change="handleCurrentChange"
        :current-page="currentPage"
        :page-sizes="[10,12,15]"
        :page-size="100"
        layout="total, sizes, prev, pager, next, jumper"
        :total="tableData.length">
      </el-pagination>
    </div>
   </div>
</template>

<script>
  import {removePancreas,getPathoInfoList,upgradePathoData} from '../../../api/api'
export default {
    name:'bingLiIndex',
  data() {
    return {
      tumorClass:[{value:'胰腺导管腺癌',label:'胰腺导管腺癌'},{value:'胰腺神经内分泌瘤',label:'胰腺神经内分泌瘤'},
        {value:'胰腺粘液性囊腺瘤',label:'胰腺粘液性囊腺瘤'}],
      filters: {
        name: '',
        type:1
				},
      typeData:[],


      tableData: [],
      currentPage: 1,
      totalData: 20,
      pagesize:10,
      editFormVisible: false,//编辑界面是否显示
      editLoading: false,
      editFormRules: {
        name: [
          {required: true, message: '请输入姓名', trigger: 'blur'}
        ]
      },
      //编辑界面数据
      editForm: {casename:'',tumorClass:'',differentiation:'',TNM:'',pk:''},
      searchItem: {casename:'',houspitalID:'',pathoID:'',tumorClass:'',differentiation:'',TNM:''}
    }
  },
  methods: {
      //显示病理图像数据
    handleUpdate(editForm){

      var postData={
        casename:this.editForm.casename,
        differentiation:this.editForm.differentiation,
        TNM:this.editForm.TNM,
        id:this.editForm.pk,
        tumorClass:this.editForm.tumorClass
      }
      console.log(postData)
      upgradePathoData(postData).then((res)=>{
        this.getPathoInfoList()
      })
      this.editFormVisible = false;

    },
    handleShowBingLi(index, row) {
        var data = Object.assign({}, row); //这句是关键！！！
        window.alert('显示'+data.fields.pathoID+'的病理图像')

    },

    getPathoInfoList() {
			let para = {
					page: this.page,
          type:this.filters.type,
					name: this.filters.name,
          houspitalID:''
				};
				this.listLoading = true;
				  getPathoInfoList(para).then((res) => {



					this.tableData=JSON.parse(res.data.data)
					this.listLoading = false;

				});
			},
    typeInfo(){
      this.typeData=[
        {value:1,label:'全部'},
        {value:2,label:'姓名'},
        {value:3,label:'病理号'},
        {value:4,label:' '},
        {value:5,label:'TNM分期'},
        {value:6,label:'癌症类型'},
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
            this.getPathoInfoList()
          })
				});
			},
    //点击编辑
    handleEdit(index, row) {
        this.editFormVisible = true;
        this.editForm = Object.assign({}, row.fields); //这句是关键！！！
        this.editForm.pk=row.pk
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
    // handleUpdate(forName) {
    //     //更新的时候就把弹出来的表单中的数据写到要修改的表格中
    //   console.log(this.editForm)
    //     var postData = {
    //         TNM: this.editForm.TNM,
    //         tumorClass:this.editForm.tumorClass,
    //         id:this.editForm.pk
    //
    //     }
    //     if (this.editForm.TNM){
    //       postData.TNM=this.editForm.TNM
    //     }else{
    //       postData.TNM=this.editForm.fields.TNM
    //     }
    //     if (this.editForm.tumor_class){
    //       postData.tumor_class=this.editForm.tumor_class
    //     }else{
    //       postData.tumor_class=this.editForm.fields.tumor_class
    //     }
    //     this.$axios.get("/api/pancreas/edit/"+postData.id+'/'+postData.TNM+'/'+postData.tumor_class).then(response =>{
		// 			  console.log('数据修改成功')
    //         this.getPathoInfoList()
    //       })
    //
    //
    //
    //     //这里再向后台发个post请求重新渲染表格数据
    //     this.editFormVisible = false;
    // }


  },
   created() {
      this.getPathoInfoList();
      this.typeInfo()//分类初始化
  },
}
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
      .el-form-item{text-align: left;}

</style>
