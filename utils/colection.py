import xlrd
import xlsxwriter
import os
import sys
import json
model="test"
if(os.getcwd().find("utils")==-1):
    model="running"
base=""
if model=="test":
    base="../workspace/"
else:
    base="./"
def load_json(i):
    out=json.load(open(base+"out/"+str(i)+"/out",'r',encoding="utf-8"))
    return out
def get_len():
    script_file = open(base + 'cmd.fio', mode='r')
    scripts = script_file.readlines()
    return len(scripts)
sec_key=["filename","bs","runtime","ioengine","direct","rw","iodepth","numjobs","r_bw","r_iops","w_bw","w_iops"]
def get_col_dic(i=1):
    json_obj=load_json(i)
    global_opt=json_obj['global options']
    jobs=json_obj['jobs'][0]
    dic={}
    dic["r_bw"]=jobs['read']['bw']
    dic["r_iops"]=jobs['read']['iops']
    dic["w_bw"]=jobs['write']['bw']
    dic["w_iops"]=jobs['write']['iops']
    col_dic=dic.copy()
    col_dic.update(global_opt)
    return col_dic
def colection():
    workbook = xlsxwriter.Workbook('../workspace/colection.xlsx')
    worksheet = workbook.add_worksheet()
    worksheet.write(0, 0, "id")
    i=1
    for key in sec_key:
        worksheet.write(0,i,key)
        i=i+1
    length=get_len()
    for j in range(1,length+1):
        col_dic=get_col_dic(j)
        i=1
        for key in sec_key:
            worksheet.write(j,i,col_dic[key])
            i=i+1
        worksheet.write(j, 0, j)
    workbook.close()

colection()

datefile = open("../workspace/date",mode='r')
date=datefile.readlines()[0]
date.replace("\n","")
s="tar  -cvf  ../workspace"+date[0:13]+".tar  ../workspace"
print(s)
os.system(s)
