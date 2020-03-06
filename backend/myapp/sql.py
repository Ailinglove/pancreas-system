import json
import os
from django.db.models import Q
import pydicom
from django.core import serializers
from .models import admin,patientBasicInfo,pathoDataInfo,imgDataInfo,tumorMarkerInfo

# 对病人基本信息的处理
def insertBasic(itemLs):

    exist = patientBasicInfo.objects.filter(patientID=itemLs[1])
    if exist.exists():
        print("this data item is existed")
    else:
        patientBasicInfo.objects.get_or_create(
        casename=itemLs[0],
        patientID=itemLs[1],
        houspitalID=itemLs[2],
        sex=itemLs[3],
        age=itemLs[4],
        BMI=itemLs[5],
        smokingH=itemLs[6],
        GeneticH=itemLs[7])
def patientBasicInfoList():
    patientList=serializers.serialize('json',patientBasicInfo.objects.all())
    return patientList
def searchBasicInfo(ID): # 查找patientID号为ID的病人
    BasicInfo=serializers.serialize('json',patientBasicInfo.objects.filter(patientID=ID))
    return BasicInfo

def deletePatient(id):
    patientBasicInfo.objects.filter(id=int(id)).delete()
    return 'success'
def upgradePatient(param):
    patientBasicInfo.objects.filter(id=int(param['id'])).update(casename=param['casename'],age=param['age'],sex=param['sex'],isExisted=param['isExisted'],tumorClass=param['tumorClass'])
    # print( serializers.serialize('json',patientBasicInfo.objects.filter(id=int(param['id']))))
    return 'success'

def imgDataInfoList(type,value):
    if type==1:#获取全部的数据
        json=serializers.serialize('json',imgDataInfo.objects.all())
    elif type==2:#查找姓名
        json=serializers.serialize('json',imgDataInfo.objects.filter(casename__icontains=value))
    elif type==3:#查找病人ID
        json=serializers.serialize('json',imgDataInfo.objects.filter(patientID =value))
    elif type==4:#查找扫描设备
        json = serializers.serialize('json', imgDataInfo.objects.filter(modality__icontains=value))

    else:#查找癌症类型
        json = serializers.serialize('json', imgDataInfo.objects.filter( reportResult__icontains=value))
    return json
def searchImgInfo(searchItem,num=0): # 查找patientID号为ID的病人
    print(searchItem)
    searchItem=json.loads(searchItem)
    ID=searchItem['patientID']
    modality=searchItem['modality']
    tumorClass=searchItem['tumorClass']
    if num==1:#处理筛选
        BasicInfo=serializers.serialize('json',imgDataInfo.objects.filter(Q(patientID=ID)|Q(modality=modality)|Q(reportResult=tumorClass)))
    elif num == 2:  # 处理按ID查找
        BasicInfo = serializers.serialize('json', imgDataInfo.objects.filter(patientID=ID))
    print('查找到',ID)
    return BasicInfo

def insertImg(imgItem):

    exist = imgDataInfo.objects.filter(patientID=imgItem[1],modality=imgItem[11],checkDate=imgItem[6],casename=imgItem[0])
    if exist.exists():
        print("this data item is existed")
        return 1
    else:
        imgDataInfo.objects.get_or_create(
            casename=imgItem[0],
            patientID=imgItem[1],
            houspitalID=imgItem[2],
            sex=imgItem[3],
            age=imgItem[4],

            checkMethod=imgItem[5],
            checkDate=imgItem[6],
            checkDevice=imgItem[7],
            imgReport=imgItem[8],
            reportResult=imgItem[9],
            imgPath=imgItem[10],modality=imgItem[11]
        )
        print('insert success!!!')
        return 0
def deleteImgData(id):
    # 要删除数据的id,(并非病人ID)，扫描时间
    imgDataInfo.objects.filter(id=int(id)).delete()
    return 'success'

def upgradeImgData(param):
    # 要删除数据的id,(并非病人ID)，更新的两个参数
    imgDataInfo.objects.filter(id=int(param['id'])).update(reportResult=param['reportResult'],modality=param['modality'],checkDate=param['checkDate'])
    return 'success'

#对病理数据信息的操作
def pathoDataInfoList(houspitalID):
    if houspitalID=='all':
        pathoDataInfoList=serializers.serialize('json',pathoDataInfo.objects.all())
    else:
        try:
            pathoDataInfoList=serializers.serialize('json', pathoDataInfo.objects.filter(houspitalID__icontains=houspitalID))
        except:
            pathoDataInfoList=''
    return pathoDataInfoList
def upgradePathoData(param):
    pathoDataInfo.objects.filter(id=int(param['id'])).update(casename=param['casename'],
                                                             tumorClass=param['tumorClass'], differentiation=param['differentiation'],TNM=param['TNM'])
    return 'success'
#对肿瘤标志物数据的操作
def tumorMarkerInfoList():
    tumorMarkerList=serializers.serialize('json',tumorMarkerInfo.objects.all())
    return tumorMarkerList







