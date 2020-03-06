<template>
  <div>
    <div class="table_container">
      <el-table :data="tableData.slice((currentPage-1)*pagesize,currentPage*pagesize)" height="500" highlight-current-row
                :default-sort = "{prop: 'fields.registerDate', order: 'descending'}"style="width: 100%;" >
<!--    <el-table :data="tableData.slice((currentPage-1)*pagesize,currentPage*pagesize)" height="500" highlight-current-row :default-sort = "{prop: 'fields.registerDate', order: 'descending'}"style="width: 100%;">-->
<!--			<el-table-column type="selection" width="55">-->
<!--			</el-table-column>-->
        <el-table-column type="index" width="100" label="序列号"></el-table-column>
        <el-table-column prop="fields.patientID" label="患者ID号" width="150" sortable></el-table-column>
        <el-table-column prop="fields.casename" label="姓名" width="150" sortable></el-table-column>
        <el-table-column prop="fields.age" label="年龄" width="80" sortable></el-table-column>
        <el-table-column prop="fields.sex" label="性别" width="80"  sortable></el-table-column>
        <el-table-column prop="fields.isExisted" label="是否有癌" sortable></el-table-column>
        <el-table-column prop="fields.tumorClass" label="癌症类型" width="180"  sortable></el-table-column>
        <el-table-column label="操作" width="280">
				<template slot-scope="scope">
          <el-button type="success" size="small" @click="handleEdit(scope.$index, scope.row)">编辑</el-button>
          <el-button type="danger" size="small" @click="handleDel(scope.$index, scope.row)">删除</el-button>

					<el-button type="info" size="small" @click="showDetails(scope.row)">详细数据</el-button>
				</template>
			</el-table-column>
		    </el-table>
    </div>
<!--    编辑界面-->
    <el-dialog title="编辑" :visible.sync="editFormVisible"
     class="edit-form" :before-close="handleClose">
       <el-form v-model="editForm" label-width="80px" :rules="editFormRules" ref="editForm">
          <el-form-item label="姓名" prop="fields.casename">
              <el-input v-model="editForm.casename " auto-complete="off"></el-input>
          </el-form-item>
         <el-form-item label="性别" prop="fields.sex">
           <el-select v-model="editForm.sex" placeholder="请选择性别">
             <el-option label="男" value="M"></el-option>
             <el-option label="女" value="F"></el-option>
           </el-select>
         </el-form-item>
          <el-form-item label="年龄" prop="fields.age">
              <el-input v-model="editForm.age " auto-complete="off"></el-input>
          </el-form-item>
         <el-form-item label="是否有癌" prop="fields.age">
           <el-select v-model="editForm.isExisted" placeholder="请选择是否有癌">
             <el-option label="有" value="有"></el-option>
             <el-option label="无" value="无"></el-option>
           </el-select>
          </el-form-item>
          <el-form-item label="癌症类型" prop="fields.age">
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
<!--    分页条-->
     <div>
           <el-pagination
            @size-change="handleSizeChange"
            @current-change="handleCurrentChange"
            :current-page="currentPage"
            :page-sizes="[7,12,15]"
            :page-size="100"
            layout="total, sizes, prev, pager, next, jumper"
            :total="tableData.length">
          </el-pagination>
     </div>
  </div>


</template>


<script>
  import {removeUsers,getPatientList,upgradePatient} from '../../../api/api'
  import {showDetails} from '../js/dataProcess'
export default {
  name: 'HelloWorld',
  data () {
    return {
      tumorClass:[{value:'胰腺导管腺癌',label:'胰腺导管腺癌'},{value:'胰腺神经内分泌瘤',label:'胰腺神经内分泌瘤'},
        {value:'胰腺粘液性囊腺瘤',label:'胰腺粘液性囊腺瘤'}],
      patientID:'',
      houspitalID:'',
      tableData:[],

      // 分页
      currentPage:1,
      totalData:20,
      pagesize:12,

      //编辑界面

      editFormVisible:false,//编辑界面是否显示
      editFormRules: {
        name: [
          {required: true, message: '请输入姓名', trigger: 'blur'}
        ]
      },
      editForm:{ //编辑界面数据
        casename:'',
        age:'',
        sex:'',
        isExisted:'',
        tumorClass:'',
        pk:''

      }
    }
  },
  methods: {
    // 更新病人信息
    handleUpdate(editForm){
      console.log(editForm)
      var postData={
        casename:this.editForm.casename,
        age:this.editForm.age,
        sex:this.editForm.sex,
        isExisted:this.editForm.isExisted,
        tumorClass:this.editForm.tumorClass,
        id:this.editForm.pk
      }
      console.log(postData)
      upgradePatient(postData).then((res)=>{
        this.getPatientList()
      })
      this.editFormVisible = false;

    },
    showDetails(row){
      console.log(row.fields)
       this.patientID=row.fields.patientID
      this.houspitalID=row.fields.houspitalID
      console.log(this.houspitalID,row.fields.houspitalID)
      this.$router.push({name:'detailInfo',params:{patientID:this.patientID,
          houspitalID:this.houspitalID}})
      console.log('跳转到：',this.houspitalID)
      // this.$router.push({name:'detailInfo',params:{patientID:this.patientID}})
    },
    unique(arr) {
        const res = new Map();
        return arr.filter((arr) => !res.has(arr.fields.patientID) && res.set(arr.fields.patientID, 1));
      },
    handleClose(done) {
        done()
      },

    // 分页处理
    handleSizeChange(pagesize) {
      this.pagesize = pagesize
      console.log(`每页 ${pagesize} 条`);
    },
    handleCurrentChange(currentPage) {
      this.currentPage = currentPage;
      console.log(`当前页: ${currentPage}`);
    },
    // 获取病人列表
    getPatientList() {
			let para = {
					page: this.page,
          patientID:'',
				};
				this.listLoading = true;
				  getPatientList(para).then((res) => {
				    this.tableData=JSON.parse(res.data.data)
            this.tableData=this.unique(this.tableData)
					  this.listLoading = false;

				});
			},
    // 编辑处理
    handleEdit(index,row){
      this.editFormVisible=true;
      this.editForm=Object.assign({},row.fields);//这句是关键
      this.editForm.pk=row.pk

    },
    },
  created() {
      this.getPatientList();

  },

}
</script>

<!-- Add "scoped" attribute to limit CSS to this component only -->
<style scoped lang="css">
h1, h2 {
  font-weight: normal;
}
ul {
  list-style-type: none;
  padding: 0;
}
li {
  display: inline-block;
  margin: 0 10px;
}
a {
  color: #42b983;
}
   .el-table td, .el-table th{
    padding: 1px;
     text-align: center;
  }
    .el-form-item__content {
    line-height: 20px;
    position: relative;
    font-size: 14px;
}
  .el-drawer{

  }
  .detailbtn{
    font-size: 14px;
  }
  .table_container{
    width: 90%;
    margin: 0 auto;
  }
  .el-form-item{text-align: left;}
  .el-input{
    width: 400px;
  }
  .el-scrollbar{
    width:10px;
  }
  .el-select-dropdown{
    max-width:100px;
  }
</style>
