from django.db import models

# 用户信息
class admin(models.Model):
    account=models.CharField(max_length=20)
    password=models.CharField(max_length=15)
    class Meta:
        db_table = "admin"
        ordering = ['id']
class patientBasicInfo(models.Model): #病人基本信息表
    # mainkey=models.CharField(max_length=15)
    casename=models.CharField(max_length=20)
    patientID=models.CharField(max_length=20)
    houspitalID = models.CharField(max_length=20)
    age = models.IntegerField()
    sex = models.CharField(max_length=2)
    BMI = models.CharField(max_length=5)
    smokingH = models.CharField(max_length=20) #吸烟史
    GeneticH = models.CharField(max_length=20) #遗传史

    isExisted=models.CharField(max_length=10)
    tumorClass=models.CharField(max_length=20)
    class Meta:
        db_table = "patientbasicinfo"
        ordering = ['id']



# 影像报告
class imgDataInfo(models.Model): # 影像数据信息
    # 病人基本信息
    # mainkey = models.CharField(max_length=15)
    casename=models.CharField(max_length=20)
    patientID=models.CharField(max_length=20)
    houspitalID = models.CharField(max_length=20)
    age=models.IntegerField()
    sex=models.CharField( max_length=2)
    #影像信息
    modality=models.CharField(max_length=10)
    checkMethod=models.CharField(max_length=20) #检查方法
    checkDate = models.CharField(max_length=20)
    checkDevice=models.CharField(max_length=10) #扫描设备

    imgReport=models.CharField(max_length=500)
    reportResult = models.CharField(max_length=20)
    uploadTime=models.DateTimeField(auto_now_add=True)
    imgPath=models.CharField(max_length=100)

    class Meta:
        db_table = "imgDataInfo" #结构化报告
        ordering = ['id']

# 病理报告
class pathoDataInfo(models.Model):
    # mainkey = models.CharField(max_length=15)
    casename=models.CharField(max_length=20)
    houspitalID = models.CharField(max_length=15)
    pathoID = models.CharField(max_length=15)
    age=models.IntegerField()
    sex=models.CharField( max_length=10) # 1代表男，0代表女

    # 病理信息
    pathoReport=models.CharField(max_length=1000) # 病理诊断报告
    tumorS=models.CharField(max_length=20) # 肿瘤来源
    size = models.CharField(max_length=30)  # 肿瘤大小
    TNM=models.CharField(max_length=10)
    differentiation=models.CharField(max_length=10) #分化
    tumorClass=models.CharField(max_length=20)#肿瘤类型
    pathoPath=models.CharField(max_length=100)

    class Meta:
        db_table = "pathoDataInfo" #结构化报告
        ordering = ['id']

class tumorMarkerInfo(models.Model):
    # 病人基本信息
    casename=models.CharField(max_length=20)
    houspitalID = models.CharField(max_length=15)
    age=models.IntegerField()
    sex=models.CharField( max_length=10) # 1代表男，0代表女

    CA199=models.CharField(max_length=10)
    CA50=models.CharField(max_length=10)
    CEA = models.CharField(max_length=10)
    CA242 = models.CharField(max_length=10)
    class Meta:
        db_table = "tumorMarkerInfo" #结构化报告
        ordering = ['id']




