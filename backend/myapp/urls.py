from django.contrib import admin
from django.views.static import serve
from django.urls import path
from django.conf.urls import url
from myapp import views
urlpatterns=[
    path('pancrease/',views.retPancrease),



]
'''
path('retPatientList/',views.ret_patientlist),
    path('user/remove/<str:id>',views.delete_patient),
    path('patient/upgrade/',views.upgrade_patient),

    #  影像数据的处理
    path('ret_pancreasinfolist/',views.retImgInfoList),
    path('pancreas/remove/<str:id>',views.deleteImgData),
    path('pancreas/upgrade/',views.editImgData),


    # 病理数据的处理
    path('retPathoInfoList/',views.retPathoInfoList),
    path('pathoData/upgrade/',views.upgrade_pathoData),

    # 肿瘤标志物的处理
    path('retTumorMarkerInfoList/',views.retTumorMarkerInfoList),

    path('testDicom/IM00001',views.testDicom),


    #文件上传
    path('fileUploader/',views.fileUploader),

# 数据显示

    path('getImgURL/',views.getImgURL),
    url(r'^showDiocm/(?P<path>.*)$',serve,{'document_root':r'D:\work\vue\DataManage\backend\static'}),


    #数据统计
    path('dataStatic/',views.static)
    '''

