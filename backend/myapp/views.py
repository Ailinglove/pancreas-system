# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.test import TestCase
from django.http import JsonResponse,HttpResponse
from myapp import sql
import os
from django.core.files.storage import default_storage
from django.core.files.base import ContentFile
from django.conf import settings
import pydicom
import pandas
from .models import *
from django.db.models.aggregates import Count

# Create your tests here.

'''
        *********************数据管理*********************
'''

#病人基本信息处理
def retPancrease(request):
    if request.method=='GET':
        data=sql.retPancrease()

        return JsonResponse({'status':0,'data':data})
    else:
        return JsonResponse({'status':1,'message':'You need GET method'})
        '''
def delete_patient(request,id):
    if request.method=='GET':
        sql.deletePatient(id)
        return JsonResponse({'status':0,'message':id})
    else:
        return JsonResponse({'status':1,'message':'You need GET method'})
def upgrade_patient(request):

    sql.upgradePatient(request.GET)
    return JsonResponse({'status':0,'message':'success'})

#影像数据信息处理
def retImgInfoList(request):
    print(request.GET)
    json = sql.imgDataInfoList(1)

    return JsonResponse({'status':0,'data':json})

def deleteImgData(request,id):
    # 要删除数据的id,(并非病人ID)，扫描时间
    if request.method=='GET':
        sql.deleteImgData(id)
        return JsonResponse({'status':0,'message':id})
    else:
        return JsonResponse({'status':1,'message':'You need GET method'})
def editImgData(request):
    # 要删除数据的id,(并非病人ID)，更新的两个参数
    if request.method=='GET':

        sql.upgradeImgData(request.GET)
        return JsonResponse({'status':0,'message':'success'
                                                  ''})
    else:
        return JsonResponse({'status':1,'message':'You need GET method'})


#病理数据信息处理
def retPathoInfoList(request):
    if request.method=='GET':
        print(request.GET)
        if request.GET['houspitalID']:
            houspitalID=request.GET['houspitalID']
            json=sql.pathoDataInfoList(houspitalID)

        else:
            json=json=sql.pathoDataInfoList('all')
        return JsonResponse({'status':0,'data':json})
    else:
        return JsonResponse({'status':1,'message':'You need GET method'})
def upgrade_pathoData(request):

    sql.upgradePathoData(request.GET)
    return JsonResponse({'status':1})

#肿瘤标志物信息处理
def retTumorMarkerInfoList(request):
    if request.method=='GET':
        json=sql.tumorMarkerInfoList()
        return JsonResponse({'status': 0, 'data': json})
    else:
        return JsonResponse({'status': 1, 'message': 'You need GET method'})


def fileUploader(request):
    print('--------------------------------------------')
    return JsonResponse({"status": 0, "num": 1})

    # num=2
    #
    # data=request.FILES.getlist('file')[0]
    # relativePath = request.POST['relativePath']
    #
    # if request.method=='POST':
    #     if fileType=='imgfile':
    #         # 处理影像数据
    #
    #         path = default_storage.save(os.path.join(r'D:\work\vue\DataManage\backend\sqlData\imgData', relativePath),
    #                                     ContentFile(data.read()))
    #
    #         try:
    #             ds=pydicom.read_file(path)
    #             imgItem=['']*12
    #             basicinfoItem = [''] * 8
    #             imgItem[0]=basicinfoItem[0]=ds.PatientName
    #             imgItem[1]=basicinfoItem[1]=str(ds.PatientID)
    #             imgItem[11] = str(ds.Modality)
    #             imgItem[6] = str(ds.StudyDate)
    #             imgItem[3]=basicinfoItem[3] = str(ds.PatientSex)
    #             imgItem[4]=basicinfoItem[4] = int(ds.PatientAge[1:3])
    #
    #
    #             num=sql.insertImg(imgItem)
    #             sql.insertBasic(basicinfoItem)
    #         except:
    #             pass
    #
    #
    #
    #
    #     if fileType == 'pathofile':
    #         # 处理病理数据
    #         print('正在处理病理数据')
    #     import xlrd
    #     if fileType=='txtfile':
    #         # 处理文本数据
    #         path = default_storage.save(os.path.join(r'D:\work\vue\DataManage\backend\sqlData\imgData', relativePath),
    #                                     ContentFile(data.read()))







def test(request):

    return JsonResponse({
        'status':0,
        'message':'meicuo'
    })

#
#


def getImgURL(request):
    root = r'D:\work\vue\DataManage\backend\static\imgData\0QG00000653'
    s = r'\api\showDiocm\imgData\0QG00000653\byCT'
    modality = 'CT'
    img = []
    resDic = {}

    modalityPath = os.path.join(root, 'by' + modality)
    imgPath = os.listdir(modalityPath)  # imgpath为存放扫描时间的目录

    serialList = os.listdir(os.path.join(modalityPath, imgPath[0]))  # 序列的路径列表
    for serial in serialList:
        serialDic = {}
        serialPath = os.path.join(modalityPath, imgPath[0], serial)
        print(len(os.listdir(serialPath)))
        thickness = os.listdir(serialPath)[0]
        # for thickness in os.listdir(serialPath):
        dcmList = [x for x in os.listdir(os.path.join(serialPath, thickness)) if 'SE' not in x]
        # for dcm in dcmList:
        #     print(os.path.join(serialPath,thickness,dcm),os.path.join(serialPath,thickness,dcm+'.dcm'))
        #     os.renames(os.path.join(serialPath,thickness,dcm),os.path.join(serialPath,thickness,dcm+'.dcm'))
        print(os.path.join(s, thickness, dcmList[0]))
        dcmPath = [os.path.join(s, imgPath[0], serial, thickness, x).replace('\\', '/') for x in dcmList]
        serialDic[thickness] = list(dcmPath)
        img.append({'name':serial,'imglist':list(dcmPath)})
    print(img)
    return JsonResponse({"status": 0, "url": img})
    # return resDic
def showDicom(request):
    imgPath=getImgURL()
    return JsonResponse({"status":0,"url":imgPath})



def static(request):
    age=patientBasicInfo.objects.values('age').annotate(count=Count('age')).order_by().values('age','count')
    return JsonResponse({"status":0,"age":age})




def testDicom(request):
    if request.method=='GET':
        dic={}
        path=r'D:\work\vue\数据管理系统\backend\sql\dcmData\1.2.392.200036.9116.2.5.1.48.1224104463.1484632471.629820'
        filmain=path
        name='IM00001'
        return JsonResponse({'status':0,'filemain':path,'value':name})
    else:
        return JsonResponse({'status':1,'message':'You need GET method'})



'''



