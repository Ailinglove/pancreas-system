import pymysql
import os
import pydicom
import pandas
def createdb(cursor):

    try:
        sql="drop table tbpancrease;"
        cursor.execute(sql)
    except:
        print('不存在此数据库表')

    # 创建表
    # classP 代表正常、慢性胰腺炎、有癌三类
    try:
        sql='create table tbpancrease (xh varchar(30) primary key,' \
            'patientID varchar(15),houspitalID varchar(15),pathoID varchar(15),casename varchar(30),sex varchar(2),age varchar(3),classP varchar(10),tumorClass varchar(20),' \
            'modality varchar(5),scanTime varchar(30),thickness varchar(100),item varchar(500),uploadTime varchar(20),' \
            'imgReportBX varchar(300),imgReportJL varchar(500),checkMethod varchar(30),' \
            'pathoZhenDuan varchar(1000),' \
            'dataPath varchar(200))'
        cursor.execute(sql)

    except:
        print('数据库表已存在！！！')

def inserData(db,table,cursor,values):
    # 添加某个关键字
    # sql='alter table tbpancrease add pathoID varchar(20) not Null;'

    # 插入一条数据
    sql="insert into {table} (xh,patientID,casename,sex,age,scanTime,modality,thickness,item,dataPath) values {values}".format(table=table,values=values)

    cursor.execute(sql)
    db.commit() # 有这一句才能插入到数据库中数据

def CHData(path,xh,db,cursor):
    caselist=os.listdir(path)
    serialItem=['DWI','T1_Inphase','T1_fat','T1+C','AX MASK','T1_water','MRCP','C-','A1','A2','P','V','T1_Outphase']
    for case in caselist:
         data,modalityPath = {},{}
         modalitylist=os.listdir(os.path.join(path,case))
         for modality in modalitylist:
             modalityDir=os.path.join(path,case,modality)
             curTime,thicknesset ,= {},set()
             for serial in os.listdir(modalityDir):
                 if not os.path.isdir(os.path.join(modalityDir,serial)):
                     continue

                 dcmlist=os.listdir(os.path.join(modalityDir,serial))
                 item = [x for x in serialItem if x in serial.split('.')[-1]]
                 if item:
                     try:
                        ds = pydicom.read_file(os.path.join(modalityDir, serial, dcmlist[0]))

                     except:
                        ds=''
                     if ds:

                         item=item[0]
                         scanTime=ds.StudyDate
                         patientID=ds.PatientID
                         casename = str(ds.PatientName)
                         modalities=ds.Modality
                         sex=ds.PatientSex
                         age=ds.PatientAge
                         try:
                            thickness= float(ds.SliceThickness)
                            thickness='{:.1f}'.format(thickness)
                         except:
                             thickness=0
                             print('no thickness')
                         data['casename']=casename
                         data['sex']=sex
                         data['age']=age
                         data['patientID']=patientID
                         curTime['modality'] = modalities
                         curTime.setdefault(thickness,set()).add(item)
                         thicknesset.add(thickness)
                         data.setdefault('scanTime', set()).add(scanTime+'_'+modalities)
                         data[scanTime+'_'+modalities]=curTime
                         modalityPath[scanTime+'_'+modalities]=modalityDir

                         data['thickness']=thicknesset
                         data['dataPath']=modalityPath
         if data:

             for scanTime in data['scanTime']:
                 items = [(key, value) for key, value in data[scanTime].items() if key != 'modality']
                 # xh为ID号+扫描时间+模态
                 xh=str(data['patientID']).zfill(11)+'_'+scanTime

                 try:
                     values = (xh, data['patientID'], data['casename'], data['sex'], data['age'][1:3],
                               scanTime, data[scanTime]['modality'], str(data['thickness']), str(items),data['dataPath'][scanTime])
                     isexistSql = "select 1 from tbpancrease where patientID = '{}' and scanTime='{}'  limit 1".format(data['patientID'],scanTime)
                     if cursor.execute(isexistSql):
                         print('该数据已经存在')
                     else:
                         inserData(db, 'tbpancrease', cursor, values)
                 except:
                     pass

def batchProcess(db,cursor):
    batchPath='/data/cleaned_data'
    item=[x for x in os.listdir(batchPath) ]
    for itemi in item:
        print(itemi)
        sql = 'select count(*) from tbpancrease;'
        cursor.execute(sql)
        db.commit()
        xh = cursor.fetchall()
        print('数据库中已有{}条数据'.format(xh[0][0]))
        CHData(os.path.join(batchPath,itemi),xh[0][0],db,cursor)
def upgradeTable_imgReport(cursor,db):
    # 从影响报告中读取数据，补充住院号，报告表现，报告结论
    # imgReportPath=r'C:\Users\刘丽\Desktop\a.xlsx'
    imgReportPath=r'/home/ll/CH数据整理/excel文件/mergeImageMedical.xlsx'
    imgReportPd=pandas.read_excel(imgReportPath,dtype='str')
    imgReportPd=imgReportPd[['患者编号', '住院号','检查日期','检查设备', '检查方法', '报告表现','报告结论']]

    #查询到所有的数据依次执行更新操作
    sql="select xh,patientID,casename,scanTime from tbpancrease"
    cursor.execute(sql)
    result=cursor.fetchall()
    for row in result:# xh 组成：0QG00024840_20190509_MR
        print('*'*30)
        patientID,scanTime,modality=row[0].split('_')[0].lstrip('0'),row[0].split('_')[1],row[0].split('_')[2]
        casename=row[2]
        print(patientID,scanTime,modality)
        dataItem=imgReportPd[imgReportPd['患者编号'].str.contains(patientID)].values.tolist()

        for case in dataItem:
            scantime=case[2].replace('-','')
            modalits=case[3][:2]
            if scanTime==scantime and modality==modalits:
                upgradeSql = "update tbpancrease set houspitalID='{}',imgReportBX='{}',imgReportJL='{}',checkMethod='{}' where xh='{}';".format(case[1],case[5],case[6],case[4],row[0])

                cursor.execute(upgradeSql)
                db.commit()
                break

def upgradeTable_PathoReport(cursor,db):
    # 从影响报告中读取数据，补充住院号，报告表现，报告结论
    # imgReportPath=r'C:\Users\刘丽\Desktop\a.xlsx'
    pathoReportPath=r'/home/ll/CH数据整理/excel文件/binglireport.xls'
    imgReportPd=pandas.read_excel(pathoReportPath,dtype='str',sheet_name='Sheet2')
    imgReportPd=imgReportPd[['住院号', '病理号','病理诊断','诊断结果']]

    #查询到所有的数据依次执行更新操作
    sql="select xh,houspitalID,dataPath from tbpancrease"
    cursor.execute(sql)
    result=cursor.fetchall()
    for row in result:# xh 组成：0QG00024840_20190509_MR

        houspitalID=row[1]
        print('*' * 30,houspitalID)
        try:
            dataItem=imgReportPd[imgReportPd['住院号']==houspitalID].values.tolist()
            case=dataItem[0]

            if len(case[3])>20:
                case[3]=''
            if '慢' in row[2]:
                case[3]='慢性胰腺炎'
            upgradeSql = "update tbpancrease set pathoID='{}',pathoZhenDuan='{}',tumorClass='{}' where xh='{}';".format(case[1],case[2],case[3],row[0])

            cursor.execute(upgradeSql)
            db.commit()
        except:
            pass
if __name__=='__main__':
    # db = pymysql.connect(user='root', password='123456', database='pancreasedb', host='localhost')
    # cursor = db.cursor()
    # createdb(cursor)
    # batchProcess(db,cursor)

    # upgradeTable_imgReport(cursor,db)
    # upgradeTable_PathoReport(cursor,db)
    # cursor.close()

    import nibabel as nib

    import matplotlib.pyplot as plt
    import numpy as np

    img = nib.load('D:\medicalImage\胰腺数据集\Task07_Pancreas\labelsTr\pancreas_178.nii')

    img_arr = np.array(img.get_fdata())
    print(img_arr.shape)
    for i in range(img_arr.shape[2]):
        print(i,img_arr[:,:,i])
        img_arr =np.squeeze(img_arr[:,:,i])

        plt.imshow(img_arr)
        plt.show()



