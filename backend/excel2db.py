import os
from django.core import serializers
os.environ.setdefault("DJANGO_SETTINGS_MODULE","backend.settings")

import django
if django.VERSION >= (1, 7):  # 自动判断版本
    django.setup()
import pandas as pd
from myapp.models import admin,pancreaseData


import datetime
def mockData(mockdataPath):
    #病人基本数据信息
    basicInfo=pd.read_excel(mockdataPath,sheet_name='patientBasicInfo')
    basicInfoData=basicInfo.fillna('')
    for index in range(basicInfoData.shape[0]):

        pancreaseData.objects.get_or_create(
            casename=basicInfoData.loc[index, 'casename'],
            patientID=basicInfoData.loc[index, 'patientID'],

            houspitalID=basicInfoData.loc[index, 'houspitalID'],
            sex=basicInfoData.loc[index, 'sex'],
            age=basicInfoData.loc[index, 'age'],
            BMI=basicInfoData.loc[index, 'BMI'],
            smokingH=basicInfoData.loc[index, 'smokingH'],
            GeneticH=basicInfoData.loc[index, 'GeneticH'],
            isExisted=basicInfoData.loc[index,'isExisted'],
            imgPath=basicInfoData.loc[index,'imgPath'],
            segres=basicInfoData.loc[index,'segres'],
            classres=basicInfoData.loc[index,'classres']

        )



if __name__=='__main__':
    mockdataPath=r'D:\school\diagSystem\backend\prodata\mockdata.xlsx'
    # from django.db.models.aggregates import Count
    # # data=serializers.serialize('json',patientBasicInfo.objects.filter())
    # age=patientBasicInfo.objects.values('age').annotate(count=Count('age')).order_by().values('age','count')
    # print(age)



    mockData(mockdataPath)
    print('Done!!!')





