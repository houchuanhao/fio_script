# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import xlrd
import xlsxwriter
import os
import sys

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print('Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

current_directory = os.path.dirname(os.path.abspath(__file__))

print('path:'+current_directory)



#base="C:/Users/dell/Desktop/pythonProject/"
base="./"
Note=open(base+'cmd.fio',mode='w')

book = xlrd.open_workbook(base+"config.xlsx")
sheet1 = book.sheets()[0]
# 数据总行数
nrows = sheet1.nrows
print('数据总行数：', nrows)
# 数据总列数
ncols = sheet1.ncols
print('表格总列数：', ncols)

def get_len(strs):
    n=0
    for s in strs:
        if(type(s)==float):
            n=n+1
            continue
        if((len(s)!=0) and ("#" not in s)):
            n=n+1
    return n
def get_cmd(s0,col_id):
    if(col_id==ncols):
        s1=s0.replace(" ","__")
        #s0=s0+"-output"
        print(s0)
        Note.writelines(s0+'\n')
        return
    row0 = str(sheet1.cell(0,col_id).value)
    row0 = row0.replace('!','')
    row0=str(row0).replace(" ","")
    col_values=sheet1.col_values(col_id)
    if("#" in row0):
        get_cmd(s0,col_id+1)
        return
    if (get_len(col_values) == 1): # only row0
        get_cmd(s0 + "-"+row0+" ",col_id+1)
        return
    for i in range(1,nrows):
        v = col_values[i]
        if("#" in str(v)):
            continue
        else:
            sv=""
            if(type(v)==float):
                sv=int(v)
            else:
                sv=v
            sv=str(sv)
            s = s0 + "-"+row0+"="+sv+" ";
            get_cmd(s ,col_id+1)
    return

def gen_workspace():
    os.system("rm "+base+"workspace/ -rf")
    os.system("mkdir workspace")
    os.system("mkdir workspace/out")
    os.system("cp "+base+"cmd.fio "+base+"workspace/cmd.fio")
    os.system("cp "+base+"config.xlsx "+base+"workspace/config.xlsx")
    os.system("cp "+base+"utils/* "+base+"workspace" )
    script_file = open(base + 'cmd.fio', mode='r')
    scripts = script_file.readlines()
    i=1
    for script in scripts:
        os.system("mkdir "+base+"workspace/out/"+str(i))
        r = open(base+"workspace/out/"+str(i)+'/r', mode='w')
        r.writelines(script)
        i= i + 1
        r.close()
    run_all = open(base +"workspace/run_all",mode='w')
    run_all.write("cd out\n")
    for j in range(1,i):
        run_all.write("cd "+ str(j)+"\n"
                                    "chmod 777 r\n"
                                    "echo "+str(j)+"\n"
                                    "cat r\n"
                                    "./r\n"
                                    "cd ..\n")
    run_all.close()
    os.system("chmod 777 "+base+"workspace/run_all")
    return
get_cmd("fio ",0)
Note.close()
gen_workspace()



exit(0)
x = sheet1.col_values(9)
print(x)
print(get_len(x))
exit(0)
x_3_y_3 = sheet1.cell(2, 2).value
print('第3行第3列的单元格的值：', x_3_y_3)
workbook = xlsxwriter.Workbook(base+"out.xlsx")
worksheet = workbook.add_worksheet()
worksheet.write(1, 1, "hellwoorld")
workbook.close()
