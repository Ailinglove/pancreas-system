<template>
<div >

  <br>
  <br>
  <br>
  <br>
		<el-table :data="tableData.slice((currentPage-1)*pagesize,currentPage*pagesize)"  v-loading="listLoading" highlight-current-row :default-sort = "{prop: 'fields.registerDate', order: 'descending'}" style="width: 100%;">
      <el-table-column type="selection" width="55">
			</el-table-column>
			<el-table-column type="index" width="60">
			</el-table-column>
			<el-table-column prop="fields.casename" label="姓名" width="150" sortable>
			</el-table-column>
			<el-table-column prop="fields.houspitalID" label="住院号" width="150" sortable>
			</el-table-column>

      <el-table-column prop="fields.age" label="年龄" width="100" sortable>
			</el-table-column>
			<el-table-column prop="fields.sex" label="性别"  width="100"sortable>
			</el-table-column>

      <el-table-column prop="fields.CEA" label="CEA" width="100" sortable>
			</el-table-column>
			<el-table-column prop="fields.CA199" label="CA19-9" width="100" sortable>
			</el-table-column>
      <el-table-column prop="fields.CA50" label="CA50" width="100" sortable>
			</el-table-column>
      <el-table-column prop="fields.CA242" label="CA242" width="100" sortable>
			</el-table-column>
		</el-table>
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
  import {removePancreas,getTumorMarkerList,editPancreas} from '../../../api/api'
export default {
  data() {
    return {

      filters: {
        name: '',
        type:1
				},
      tableData: [],
      currentPage: 1,
      totalData: 20,
      pagesize:15,
    }
  },
  methods: {
    getTumorMarkerList() {
			let para = {
					page: this.page,
          type:this.filters.type,
					name: this.filters.name
				};
				this.listLoading = true;
				  getTumorMarkerList(para).then((res) => {
            this.tableData=JSON.parse(res.data.data)
					  this.listLoading = false;

				});
			},
    handleSizeChange(pagesize) {
      this.pagesize = pagesize

    },
    handleCurrentChange(currentPage) {
      this.currentPage = currentPage;

    },



  },
   created() {
      this.getTumorMarkerList();

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
  .el-table{



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
