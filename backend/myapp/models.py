from django.db import models

# 用户信息
class admin(models.Model):
    account=models.CharField(max_length=20)
    password=models.CharField(max_length=15)
    class Meta:
        db_table = "admin"
        ordering = ['id']
class pancreaseData(models.Model): #病人基本信息表
    # mainkey=models.CharField(max_length=15)
    casename=models.CharField(max_length=20)
    sex = models.CharField(max_length=2)
    age = models.IntegerField()

    patientID=models.CharField(max_length=20)
    houspitalID = models.CharField(max_length=20)
    smokingH = models.CharField(max_length=20) #吸烟史
    GeneticH = models.CharField(max_length=20) #遗传史

    isExisted=models.CharField(max_length=10)

    modality = models.CharField(max_length=10)

    classres = models.CharField(max_length=20)  #分类结果
    segres = models.CharField(max_length=20) #分割结果
    imgPath= models.CharField(max_length=100) #数据存储路径

    status= models.IntegerField(default=0) #预测状态

    BMI = models.CharField(max_length=5)

    class Meta:
        db_table = "pancreasedata"
        ordering = ['id']





