import Vue from 'vue'
import Router from 'vue-router'
//数据采集组件
import Upload from '@/components/DataCollection/dataUpload'
import Download from '@/components/DataCollection/dataDownload'


//数据管理组件
import UserList from '@/components/DataManage/PatientList/userlist'
import YXIndex from '@/components/DataManage/YingXiangData/pancreasData'
import BLIndex from '@/components/DataManage/BingLiData/bingLiIndex'
import GYIndex from '@/components/DataManage/GeneData/geneIndex'
import LCIndex from '@/components/DataManage/LinChuangData/linChuangIndex'
import TMIndex from '@/components/DataManage/TumorMarkerData/tumorMarkerIndex'
import DetailInfor from '@/components/DataManage/PatientList/detailInfo'
import Home from '@/components/Home'
import Main from '@/components/Main'
import Setting from '@/components/settings'

// 数据统计组件
import DiseaseStatic from '@/components/DataStatic/DiseaseSpeciesStatic'
import PatientStatic from '@/components/DataStatic/patientStatic'

import ModalityStatic from '@/components/DataStatic/modalityStatic'


import MainPage from '@/page/mainPage/mainIndex'


import chart from '@/components/Echarts/index'
import Login from '@/components/login/index'

import testShow from '@/components/showdicom/testShow'

import hello from '@/components/showdicom/HelloWorld'
Vue.use(Router)

export default new Router({
  routes: [
    {
      path:'/login',
      component:Login,
      name: 'login',
      hidden: true
    },
    {
      path:'/hello',
      component:hello,
      name: 'hello',
      hidden: true
    },
    {
      path:'/database/pancrease/datacollection',
      component:Home,
      name:'数据采集',
      children: [
            { path: '/database/pancrease/datacollection/upload', component: Upload, name: '数据上传' },
            { path: '/database/pancrease/datacollection/download',component: Download, name: '数据下载' },

      ]
    },
    {
        path: '/database/pancrease/dataManagement',
        component: Home,
        name: '胰腺数据管理',
        children: [
            { path: '/database/pancrease/dataManagement/userlist', component: UserList, name: '病人信息管理' },
            { path: '/database/pancrease/dataManagement/YXDataManagement', component: YXIndex, name: '影像数据管理' },
            { path: '/database/pancrease/dataManagement/BLDataManagement', component: BLIndex, name: '病理数据管理' },
            { path: '/database/pancrease/dataManagement/GYDataManagement', component: GYIndex, name: '基因数据管理' },
            { path: '/database/pancrease/dataManagement/TMDataManagement', component: TMIndex, name: '肿瘤标志物' },
        ]
    },
    {
        path: '/database/pancrease/datastatic',
        component: Home,
        name: '统计分析管理',
        children: [
          { path: '/database/pancrease/datastatic/patientStatic', component: PatientStatic, name: '按患者统计分析' },
          { path: '/database/pancrease/datastatic/diseaseSpecoesStatic', component: DiseaseStatic, name: '按病种统计分析' },
          { path: '/database/pancrease/datastatic/modalityStatic', component: ModalityStatic, name: '按模态统计分析' }

          ]
    },
    {
        path: '/database/pancrease/settings',
        component: Setting,
        name: '',
        leaf: true,//只有一个节点
        children: [
            { path: '/database/pancrease/settings', component: Setting, name: '系统设置' }
        ]
    },

    {
      path: '/testshow',
      name: 'testShow',
      component: testShow,
      leaf: true,//只有一个节点
        children: [
            { path: '/dicomShow', component: testShow, name: 'Dicom' }
        ]
    },
    {
      path: '/detailInfo/:patientID/:houspitalID',
      name: 'detailInfo',
      component: DetailInfor,
      hidden: true
    },
    {path:'/',
      component:MainPage,
      name:'mainPage',
      hidden:true
},
  ]

})
