from django.contrib import admin
from . import models
# Register your models here.
admin.site.register(models.admin) #管理员
admin.site.register(models.imgDataInfo) #影像数据信息
admin.site.register(models.pathoDataInfo) # 病理数据信息
admin.site.register(models.tumorMarkerInfo) # 肿瘤标志物信息
admin.site.register(models.patientBasicInfo) #病人基本信息
#
# def makesentense(n):
#     import re
#     with open('adj.txt') as f1:
#         adjlist = re.split(',', f1.read())
#     with open('noun.txt') as f2:
#         nounlist = re.split(',', f2.read())
#     with open('verb.txt') as f3:
#         verblist = re.split(',', f3.read())
#     speechPartsDict = {'adj': adjlist, 'noun': nounlist, 'verb': verblist}
#
#     result = []
#     for x in range(0, n):
#         example = 'The adj noun verb.'
#         import random
#         example = example.replace('adj', random.sample(speechPartsDict['adj'], 1)[0])
#         example = example.replace('noun', random.sample(speechPartsDict['noun'], 1)[0])
#         example = example.replace('verb', random.sample(speechPartsDict['verb'], 1)[0])
#         result.append(example)
#
#     return result
#
#
# if __name__ == '__main__':
#     while True:
#         m = input('请输入需要创建的句子数目:')
#         try:
#             n = int(m)
#         except ValueError:
#             print('输入有误，重新输入...')
#         else:
#             result = makesentense(int(m))
#             i = 1
#             for x in result:
#                 print(i, '.', x)
#                 i = i + 1
#             break



