import os
from django.core import serializers
os.environ.setdefault("DJANGO_SETTINGS_MODULE","backend.settings")

import django
if django.VERSION >= (1, 7):  # 自动判断版本
    django.setup()
import pandas as pd
from myapp.models import admin,patientBasicInfo,pathoDataInfo,imgDataInfo,tumorMarkerInfo


import datetime
def mockData(mockdataPath):
    #病人基本数据信息
    basicInfo=pd.read_excel(mockdataPath,sheet_name='patientBasicInfo')
    basicInfoData=basicInfo.fillna('')
    for index in range(basicInfoData.shape[0]):

        patientBasicInfo.objects.get_or_create(
            casename=basicInfoData.loc[index, 'casename'],
            patientID=basicInfoData.loc[index, 'patientID'],

            houspitalID=basicInfoData.loc[index, 'houspitalID'],
            sex=basicInfoData.loc[index, 'sex'],
            age=basicInfoData.loc[index, 'age'],
            BMI=basicInfoData.loc[index, 'BMI'],
            smokingH=basicInfoData.loc[index, 'smokingH'],
            GeneticH=basicInfoData.loc[index, 'GeneticH'],
            isExisted=basicInfoData.loc[index,'isExisted'],
            tumorClass=basicInfoData.loc[index,'tumorClass']

        )

    #影像数据信息
    imgInfo = pd.read_excel(mockdataPath, sheet_name='imgDataInfo')
    imgInfoData = imgInfo.fillna('')
    for index in range(imgInfoData.shape[0]):
        print(imgInfoData.iloc[index, :].values.tolist())
        imgDataInfo.objects.get_or_create(
            casename=imgInfoData.loc[index, 'casename'],
            patientID=imgInfoData.loc[index, 'patientID'],
            houspitalID=imgInfoData.loc[index, 'houspitalID'],
            sex=imgInfoData.loc[index, 'sex'],
            age=imgInfoData.loc[index, 'age'],
            modality=imgInfoData.loc[index,'checkDevice'][:2],
            checkMethod=imgInfoData.loc[index, 'checkMethod'],
            checkDate=imgInfoData.loc[index, 'checkDate'],
            checkDevice=imgInfoData.loc[index, 'checkDevice'],
            imgReport = imgInfoData.loc[index, 'imgReport'],
            reportResult = imgInfoData.loc[index, 'reportResult'],
            imgPath = imgInfoData.loc[index, 'imgPath'])
    #病理数据信息
    pathoInfo = pd.read_excel(mockdataPath, sheet_name='pathoDataInfo')
    pathoInfoData = pathoInfo.fillna('')
    for index in range(pathoInfoData.shape[0]):
        print(pathoInfoData.iloc[index, :].values.tolist())
        pathoDataInfo.objects.get_or_create(
            casename=pathoInfoData.loc[index, 'casename'],

            houspitalID=pathoInfoData.loc[index, 'houspitalID'],
            pathoID=pathoInfoData.loc[index, 'pathoID'],
            sex=pathoInfoData.loc[index, 'sex'],
            age=pathoInfoData.loc[index, 'age'],

            pathoReport=pathoInfoData.loc[index, 'pathoReport'],
            tumorS=pathoInfoData.loc[index, 'tumorS'],
            size=pathoInfoData.loc[index, 'size'],
            TNM=pathoInfoData.loc[index, 'TNM'],
            differentiation=pathoInfoData.loc[index, 'differentiation'],
            tumorClass=pathoInfoData.loc[index, 'tumorClass'],
            pathoPath=pathoInfoData.loc[index, 'pathoPath'])
    # 肿瘤标志物信息
    tumormarkerInfo = pd.read_excel(mockdataPath, sheet_name='tumorMarkerInfo')
    markerInfoData = tumormarkerInfo.fillna('')
    for index in range(markerInfoData.shape[0]):
        tumorMarkerInfo.objects.get_or_create(
            casename=markerInfoData.loc[index, 'casename'],
            houspitalID=markerInfoData.loc[index, 'houspitalID'],
            sex=markerInfoData.loc[index, 'sex'],
            age=markerInfoData.loc[index, 'age'],

            CA199=markerInfoData.loc[index, 'CA199'],
            CA50=markerInfoData.loc[index, 'CA50'],
            CEA=markerInfoData.loc[index, 'CEA'],
            CA242=markerInfoData.loc[index, 'CA242'])


if __name__=='__main__':
    mockdataPath=r'D:\work\vue\DataManage\backend\prodata\mockdata.xlsx'
    # from django.db.models.aggregates import Count
    # # data=serializers.serialize('json',patientBasicInfo.objects.filter())
    # age=patientBasicInfo.objects.values('age').annotate(count=Count('age')).order_by().values('age','count')
    # print(age)



    # mockData(mockdataPath)
    # print('Done!!!')





