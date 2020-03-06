<template>
<div>
<!--  搜索栏-->
  <el-col :span="24" class="wrap-breadcrum">
    	<el-col :span="24" class="toolbar" style="padding-bottom: 20px;">
			<el-form v-model="searchItem" :inline="true" :model="filters" style="text-align: center;" size="mini" label-position="right" label-width="120px">

        <el-form-item label="患者ID号:"><el-input v-model="searchItem.patientID" label="patientID"></el-input></el-form-item>
        <el-form-item style="width: 100px">
              <el-button type="primary" class="el-icon-search" @click="searchandle" >搜索</el-button>
        </el-form-item>
        <el-form-item label="模态：">
          <el-select v-model="searchItem.modality" placeholder="请选择，默认CT" style="width:100px">
            <el-option value="CT" label="CT" ></el-option>
            <el-option value="MRI" label="MRI"></el-option>
          </el-select>
        </el-form-item>
        <el-form-item label="癌症类型：" >
          <el-select  v-model="searchItem.tumorClass" >
            <el-option v-for="item in tumorClass" :key="item.value" :label="item.label" :value="item.value"></el-option>
          </el-select>
        </el-form-item>
				<el-form-item style="width: 100px">
              <el-button type="primary" class="el-icon-search" @click="handlefilter" style="position: fixed;right: 260px;">筛选</el-button>
        </el-form-item>
        <el-form-item >
              <el-button type="primary" class="el-icon-search" @click="getPancreasData" >全部</el-button>
        </el-form-item>

			</el-form>
		</el-col>
  </el-col>


		<el-table :data="tableData.slice((currentPage-1)*pagesize,currentPage*pagesize)"  v-loading="listLoading" highlight-current-row
              :default-sort = "{prop: 'fields.registerDate', order: 'descending'}"
              style="width: 100%;" @row-dblclick="showDetails">
			<el-table-column type="expand">
        <template slot-scope="props" >

          <el-form label-position="left" inline  class="demo-table-expand">
            <el-form-item label="影像报告" >
              <span class="item_content">{{props.row.fields.imgReport}}</span>
            </el-form-item>
          </el-form>
        </template>
      </el-table-column>


      <el-table-column type="selection" width="50"></el-table-column>
			<el-table-column type="index" width="100" label="序列号"></el-table-column>
      <el-table-column prop="fields.patientID" label="患者ID号" width="120" sortable></el-table-column>
<!--			<el-table-column prop="fields.casename" label="姓名" width="150" sortable></el-table-column>-->
			<el-table-column prop="fields.reportResult" label="癌症类型" width="180" sortable></el-table-column>

      <el-table-column prop="fields.modality" label="模态" width="80" sortable></el-table-column>
			<el-table-column prop="fields.checkDate" label="扫描时间"  width="150"sortable></el-table-column>

      <el-table-column prop="fields.uploadTime" label="上传时间" width="240" sortable>
			</el-table-column>
			<el-table-column label="操作" width="280">
				<template slot-scope="scope">

					<el-button size="small" type="success" class="el-icon-edit" @click="handleEdit(scope.$index, scope.row)">编辑</el-button>
					<el-button type="danger" size="small" @click="handleDel(scope.$index, scope.row)">删除</el-button>
				      <el-button type="info" size="small" @click="handleShowDCM(scope.$index, scope.row)">显示图像</el-button>
        </template>
			</el-table-column>
		</el-table>


    <el-dialog title="编辑"
     :visible.sync="editFormVisible"
     :close-on-click-modal="false"
     class="edit-form"
     :before-close="handleClose">
      <el-form v-model="editForm" label-width="80px" :rules="editFormRules" ref="editForm">
          <el-form-item label="癌症类型" prop="fields.tumorClass">
             <el-select v-model="editForm.reportResult" placeholder="请选择" value="">
                <el-option
                  v-for="item in tumorClass"
                  :key="item.value"
                  :label="item.label"
                  :value="item.value">
                </el-option>
            </el-select>
          </el-form-item>
        <el-form-item label="模态" prop="fields.modality">
              <el-select v-model="editForm.modality">
                <el-option label="CT" value="CT"></el-option>
                <el-option label="MR" value="MR"></el-option>
              </el-select>
          </el-form-item>

        <el-form-item label="扫描时间" prop="fields.checkDate">
          <el-input v-model="editForm.checkDate" ></el-input>
<!--            <el-date-picker v-model="editForm.checkDate" type="date" placeholder="请选择上传日期"></el-date-picker>-->
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
  import {removePancreas,getPancreasList,upgradeImgData} from '../../../api/api'
export default {
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
      editForm: {reportResult:'', modality:'', checkDate:'', pk:''},
      searchItem:{casename:'',patientID:'',modality:'CT',tumorClass:'',checkDate:''}
    }
  },
  methods: {
    showDetails(row){
      console.log('点击当前行',row)
       this.patientID=row.fields.patientID
      this.houspitalID=row.fields.houspitalID
      this.$router.push({name:'detailInfo',params:{patientID:this.patientID,
          houspitalID:this.houspitalID}})
    },
     handleShowDCM(index, row) {
        var data = Object.assign({}, row); //这句是关键！！！,深拷贝

        this.$router.push({name:'testShow'})
        // window.alert('显示'+data.fields.patientID+' 的影像数据')

    },
    handlefilter(){
      //按找条件筛选
      let para = {
					page: this.page,
          type:this.filters.type,
					name: this.filters.name,
          patientID:this.searchItem.patientID,
          searchItem:this.searchItem,
          searchClick:'2'
				};

				this.listLoading = true;
				  getPancreasList(para).then((res) => {
				    this.tableData=JSON.parse(res.data.data)
            this.tableData.forEach(function (item,index,array) {
              item.fields.uploadTime=new Date(item.fields.uploadTime).toLocaleString()
            })
					  this.listLoading = false;


				})
    },
    searchandle(){
      //查找ID号
      let para = {
					page: this.page,
          type:this.filters.type,
					name: this.filters.name,

          modality:'CT',
          searchItem:this.searchItem,
        searchClick:'1'
				};

				this.listLoading = true;
				  getPancreasList(para).then((res) => {
				    this.tableData=JSON.parse(res.data.data)
            this.tableData.forEach(function (item,index,array) {
              item.fields.uploadTime=new Date(item.fields.uploadTime).toLocaleString()
            })
					  this.listLoading = false;


				})
    },
    getPancreasData() {
			let para = {
					page: this.page,
          type:this.filters.type,
					name: this.filters.name,

          modality:'CT',
          searchItem:this.searchItem,
        searchClick:'0'
				};

				this.listLoading = true;
				  getPancreasList(para).then((res) => {
				    this.tableData=JSON.parse(res.data.data)
            this.tableData.forEach(function (item,index,array) {
              item.fields.uploadTime=new Date(item.fields.uploadTime).toLocaleString()
            })
					  this.listLoading = false;


				});
			},
    typeInfo(){
      this.typeData=[
        {value:1,label:'全部'},
        {value:2,label:'姓名'},
        {value:3,label:'病人ID'},
        {value:4,label:'模态'},
        {value:5,label:'癌症类型'},
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
        this.editForm = Object.assign({}, row.fields); //这句是关键！！！

      this.editForm.pk=row.pk
              console.log('.....',this.editForm)
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
  handleUpdate(editForm){
      var postData={
        reportResult:this.editForm.reportResult,
        modality:this.editForm.modality,
        checkDate:this.editForm.checkDate,
        id:this.editForm.pk
      }
      upgradeImgData(postData).then((res)=>{
        this.getPancreasData()
      })
      this.editFormVisible = false;

    },

  },
   created() {
      this.getPancreasData();
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
.el-form-item{text-align: center;}
    .el-input{
    width:150px;
  }
</style>
