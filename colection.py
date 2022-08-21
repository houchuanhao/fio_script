import xlrd
import xlsxwriter
import os
import sys
import json
model="test"
base=""
if model=="test":
    base="./workspace/out/"
else:
    base="./out/"
def load_json(i):
    out=json.load(open(base+str(i)+"/out.json",'r',encoding="utf-8"))
    return out
def colection(i):
    json_obj=load_json(i)
    global_opt=json_obj['global options']
    rw=global_opt['rw']
    print(rw)
    jobs=json_obj['jobs'][0]
    dic={}
    dic["r_bw"]=jobs['read']['bw']
    dic["r_iops"]=jobs['read']['iops']
    dic["w_bw"]=jobs['write']['bw']
    dic["w_iops"]=jobs['write']['iops']
    workbook = xlsxwriter.Workbook('D:/Ezra/fio_script/workspace/colection.xlsx')
    worksheet = workbook.add_worksheet()
    row=col=0
    worksheet.write(0,0,"id")
    col_dic=dic.copy()
    col_dic.update(global_opt)
    i=1
    for key in col_dic:
        worksheet.write(0,i,key)
        i=i+1
    for j in range(1,2):
        i=1
        for key in col_dic:
            worksheet.write(j,i,col_dic[key])
            i=i+1
    workbook.close()

colection(1)