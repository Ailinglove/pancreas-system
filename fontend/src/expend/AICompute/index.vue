<template>
  <div class="aiCompute">


    <div style="margin:0 auto;width: 100%;height: 100%;background-color: rgba(0,0,0,0.3)">

      <router-view></router-view>
<!--      <div style="width: 100%;height: 100%;">-->
<!--        <div class="layout left">-->
<!--          <el-table :data="tableData"-->
<!--                    style="width: 80%;color: #49494a;margin: 0 auto;border-radius: 10px;-->
<!--                      height: 80%;overflow: auto"-->
<!--                    :row-class-name="tableRowClassName"-->
<!--                    :header-cell-style="getRowClass">-->

<!--            <el-table-column label="可分析数据" align="center" width="150">-->
<!--              <template slot-scope="scope">-->
<!--                <span>{{ scope.row.name }}</span>-->
<!--              </template>-->
<!--            </el-table-column>-->
<!--            <el-table-column label="CT数据" align="center">-->
<!--              <template slot-scope="scope">-->
<!--                <span>{{ scope.row.CT | isSupported}}</span>-->
<!--              </template>-->
<!--            </el-table-column>-->
<!--            <el-table-column label="MRI数据" align="center">-->
<!--              <template slot-scope="scope">-->
<!--                <span>{{ scope.row.MRI | isSupported}}</span>-->
<!--              </template>-->
<!--            </el-table-column>-->

<!--          </el-table>-->


<!--        </div>-->
<!--        <div class="layout right">-->
<!--          <ul style="width:80%;margin:0 auto;height:100%;display: flex;list-style: none;align-content: center; flex-wrap: wrap;">-->
<!--           <li v-for="data in type" class="suanfali">-->
<!--             <router-link :to="{name: data.path}"  >-->
<!--               <div class="lidiv" style="width: 100%;height: 100%;margin:0 auto;padding-top: 30px;">-->
<!--                 <p style="font-size: 20px;padding: 30px 0;">{{data.name}}</p>-->
<!--                 <p style="font-size: 16px;padding: 0 10px; color: darkgray">{{data.intro}}</p>-->

<!--               </div>-->
<!--             </router-link>-->



<!--            </li>-->
<!--          </ul>-->
<!--        </div>-->
<!--      </div>-->

    </div>

  </div>

</template>

<style>
  .table {
    width: 900px;
    height: 400px;
    margin: 100px auto;
  }

  /*更改表格颜色*/
  .double {
    background: #f6f6f6 !important;
  }
  .single {
    background: #ccc !important;
  }

  *{
    box-sizing: content-box;
  }
  .aiCompute{
    background:  url("../../../static/bg3.jpg") no-repeat;
    background-size: 100% 100%;
    height: 100%;
    overflow: hidden;
    color: white;
    display: flex;
    align-items: center;
    justify-content: space-between;
    flex-direction: row;
    flex-wrap: wrap;

  }
  .layout{
    /*width: 50%;*/
    height: 80%;
    width: 50%;
    float: left;
    position: relative;

  }
  .right{
    background-color: rgba(255,255,255,0.4);
    border-radius: 10px;
    float: left;
  }
  .left{
    width: 30%;

    border-radius: 10px;
    background-color: rgba(0,0,0,0);
    position: relative;
    top: 50%;

    transform: translate(0,-50%);
  }

  .suanfali{
    width: 250px;height: 250px;
    margin: 20px 10px;
    border: 1px solid gray;
    background-color: rgba(0,0,0,0.7);
    border-radius: 10px;
    box-shadow: 10px 10px 10px black;
  }
  .suanfali:hover{
    box-shadow: 10px 10px 10px #156798;
    cursor: pointer;
  }
  .title{
    color: white;
    margin: 5px auto;
  }
</style>

<script>
  export default {
    name: '',
    data () {
      return {
        type:[{
          intro:'分类算法，根据病种以及类型，将图像分类',
          name:'疾病分类',
          path:'classify'
        },{
          intro: '分割算法，勾勒病灶点的边界',
          name:'肿瘤分割',
          path:'segment'
        },{
          intro:'定位算法，对肿瘤的位置进行精准的定位',
          name:'肿瘤定位',
          path:'location'
        },
          {
            intro:'添加方法',
            name:'其它诊断方法',
            path:'other'
          }],
        tableData: [ {name:'心脑血管数据',CT:1,MRI:1},
          {name:'脑部数据',CT:0,MRI:1},
          {name:'致盲性眼病数据',CT:1,MRI:1},
          {name:'乳腺肿瘤数据',CT:1,MRI:1},
          {name:'胰腺数据',CT:1,MRI:1},
          {name:'肝癌数据',CT:1,MRI:1},
          {name:'肺结节数据',CT:1,MRI:0},
          {name:'肠胃数据',CT:1,MRI:0},
        ],
      }  },
    filters:{
      isSupported(value){  // 过滤器：value
        if(value===1){
          return '支持'
        }else{
          return '尚未支持'
        }


      }
    },
    methods: {

      tableRowClassName ({ row, rowIndex }) {
        if ((rowIndex + 1) % 2 === 0) {
          return 'double';
        } else {
          return 'single';
        }
      }, getRowClass ({ rowIndex }) {
        if (rowIndex == 0) {
          return 'background:#ebeaef'
        } else {
          return ''
        }

      },

    }
  }
</script>
