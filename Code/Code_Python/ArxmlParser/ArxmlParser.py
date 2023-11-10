"""
@Time ： 2023/4/10 14:58
@Auth ： Wang Zi
@File ：ArxmlParser.py
@IDE ：PyCharm
"""
# -*- coding=utf-8 -*-
# Import the required modules
import xmltodict
import pprint
import xlwt
import subprocess
import time
import openpyxl
import tkinter
import tkinter.messagebox as msgbox
import os
import shutil
import linecache
from openpyxl import Workbook
from tkinter import filedialog
from tkinter import *


def Run_Bat():
    # cmd = 'cmd.exe c:\\sam.bat'
    p = subprocess.Popen("cmd.exe /c" + "extract_lifm_cnf.bat",
                         stdout=subprocess.PIPE,
                         stderr=subprocess.STDOUT)


xquery_path = ""
arxml_path = ""
map_path = ""
List_Dict_Time = 0
List_List_Time = 0
Total_Dict = []
count = 0
addressContext = ''
text = ''
address_str = ''


def Convert_xml_to_Dict(filename):
    global List_Dict_Time
    global List_List_Time

    with open(filename, 'r', encoding='utf-8') as file:
        my_xml = file.read()

    my_dict = xmltodict.parse(my_xml)
    for x in my_dict['icsp_lifm']['Area']:
        x = x['Blocks']['Block']
        type_str = str(type(x))
        if type_str.find('dict') != -1:
            Total_Dict.append(x)
        elif type_str.find('list') != -1:
            for z in x:
                List_List_Time = List_List_Time + 1
                Total_Dict.append(z)
            List_List_Time = 0
        List_Dict_Time = List_Dict_Time + 1

def Address_Find(xmlstr, mapstr, namestr):
    global count, addressContext, text, address_str
    xmlFiles = open(xmlstr, "r")
    for line in xmlFiles.readlines():
        if namestr in line:
            text = line
            break
        count += 1

    while text.find('Label>') == -1:
        count = count - 1
        text = linecache.getline(xmlstr, count)

    address_str = text[(text.find('Label>') + 6):text.find('</')]
    count = 0
    mapFiles = open(mapstr, "r")
    for line in mapFiles.readlines():
        if address_str in line:
            addressContext = line
            break
        count += 1
    count = 0
    address = addressContext[addressContext.find('0x'): addressContext.find('0x') + 10]
    address = '0x' + address[2:].upper()
    xmlFiles.close()
    mapFiles.close()
    return address

def Save_To_Excel(yourdict):
    times = 0
    i = 1
    Total_List = []
    Total_List_Cycle_Times = 0

    workbook = Workbook()
    sheet = workbook.active
    f = xlwt.Workbook()
    sheet1 = f.add_sheet('Lif', cell_overwrite_ok=True)
    sheet2 = f.add_sheet('Block', cell_overwrite_ok=True)

    # 样式1
    style = xlwt.XFStyle()
    mystyle = xlwt.Alignment()
    mystyle.horz = 0x02
    mystyle.vert = 0x01
    style.alignment = mystyle

    # 样式2
    style_title = xlwt.XFStyle()
    myfond = xlwt.Font()
    mystyle_title = xlwt.Alignment()
    mystyle_title.horz = 0x02
    mystyle_title.vert = 0x01
    myfond.bold = True
    style_title.font = myfond
    style_title.alignment = mystyle_title

    while times < len(yourdict):
        Lifs_Str = str(yourdict[i - 1]['Lifs'])
        Lifs_Str = Lifs_Str.replace(",", '\n')
        sheet2.write(i, 0, yourdict[i - 1]['Name'], style)
        sheet2.write(i, 1, int(yourdict[i - 1]['Offset']), style)
        sheet2.write(i, 2, int(yourdict[i - 1]['Size']), style)
        sheet2.write(i, 3, Lifs_Str, style)
        type_unit = str(type(yourdict[i - 1]['Lifs']['Lif']))
        if type_unit.find('dict') != -1:
            Total_List.append(yourdict[i - 1]['Lifs']['Lif'])
        elif type_unit.find('list') != -1:
            for dictlist in yourdict[i - 1]['Lifs']['Lif']:
                Total_List.append(dictlist)
        i = i + 1
        times += 1
    if var_mapflag.get():
        while Total_List_Cycle_Times < len(Total_List):
            sheet1.write(Total_List_Cycle_Times + 1, 0, Total_List[Total_List_Cycle_Times]['Name'], style)
            sheet1.write(Total_List_Cycle_Times + 1, 1, Total_List[Total_List_Cycle_Times]['Offset'], style)
            sheet1.write(Total_List_Cycle_Times + 1, 2, Total_List[Total_List_Cycle_Times]['NbElem'], style)
            sheet1.write(Total_List_Cycle_Times + 1, 3, Total_List[Total_List_Cycle_Times]['Type'], style)

            addressTemp = Address_Find('output.xml', 'myMap.map', Total_List[Total_List_Cycle_Times]['Name'])
            offset = int(Total_List[Total_List_Cycle_Times]['Offset'])
            addrestfact = int(addressTemp, 16) + int(offset)
            addrestfact = hex(addrestfact)
            addrestfact =  '0x' + addrestfact[2:].upper()
            print("计算地址中..." + '\n' + addrestfact)
            sheet1.write(Total_List_Cycle_Times + 1, 4, addrestfact, style)
            Total_List_Cycle_Times = Total_List_Cycle_Times + 1
    else:
        while Total_List_Cycle_Times < len(Total_List):
            sheet1.write(Total_List_Cycle_Times + 1, 0, Total_List[Total_List_Cycle_Times]['Name'], style)
            sheet1.write(Total_List_Cycle_Times + 1, 1, Total_List[Total_List_Cycle_Times]['Offset'], style)
            sheet1.write(Total_List_Cycle_Times + 1, 2, Total_List[Total_List_Cycle_Times]['NbElem'], style)
            sheet1.write(Total_List_Cycle_Times + 1, 3, Total_List[Total_List_Cycle_Times]['Type'], style)
            sheet1.write(Total_List_Cycle_Times + 1, 4, "用户选择不检索地址", style)
            Total_List_Cycle_Times = Total_List_Cycle_Times + 1

    Col_List_sheet1 = ["LifName", "LifOffset", "LifNbElem", "LifType", "LifAddress"]
    for i in range(0, 5):
        sheet1.write(0, i, Col_List_sheet1[i], style_title)
        sheet1.col(i).width = 256 * 30

    Col_List_sheet2 = ["BlockName", "BlockOffset", "BlockSize", "BlockLifs"]
    for i in range(0, 4):
        sheet2.write(0, i, Col_List_sheet2[i], style_title)
        sheet2.col(i).width = 256 * 30

    f.save('Output.xls')




# 按钮控件
def get_path_arxml():
    global entry_text
    global arxml_path
    # 返回一个字符串，且只能获取文件夹路径，不能获取文件的路径。
    # path = filedialog.askdirectory(title='请选择一个目录')
    # 返回一个字符串，可以获取到任意文件的路径。
    arxml_path = filedialog.askopenfilename(title='请选择文件', filetypes=(("Arxml Files", "*.arxml"),))
    filetypes = (('text files', '*.txt'), ('All files', '*.*'))

    currentpath_arxml = os.path.abspath('')
    currentpath_arxml = currentpath_arxml.replace('\\', '/')
    arxml_path = arxml_path.replace('\\', '/')
    currentpath_arxml = currentpath_arxml + "/icsp_lifm_cnf.arxml"
    # print(currentpath_arxml)
    shutil.copy(arxml_path, currentpath_arxml)
    # 生成保存文件的对话框， 选择的是一个文件而不是一个文件夹，返回一个字符串。
    # path = filedialog.asksaveasfilename(title='请输入保存的路径')

    entry_text_arxml.set(arxml_path)


def get_path_xquery():
    global entry_text
    global xquery_path

    xquery_path = filedialog.askopenfilename(title='请选择文件', filetypes=(("XQuery Files", "*.xq"),))
    filetypes = (('text files', '*.txt'), ('All files', '*.*'))

    currentpath_xquery = os.path.abspath('')
    currentpath_xquery = currentpath_xquery.replace('\\', '/')
    xquery_path = xquery_path.replace('\\', '/')
    currentpath_xquery = currentpath_xquery + "/extract_lifm_cnf.xq"
    shutil.copy(xquery_path, currentpath_xquery)

    entry_text_xquery.set(xquery_path)


def index_address():
    global entry_text
    global map_path

    map_path = filedialog.askopenfilename(title='请选择文件', filetypes=(("MAP Files", "*.map"),))
    filetypes = (('text files', '*.txt'), ('All files', '*.*'))

    currentpath_map = os.path.abspath('')
    currentpath_map = currentpath_map.replace('\\', '/')
    map_path = map_path.replace('\\', '/')
    currentpath_map = currentpath_map + "/myMap.map"
    shutil.copy(map_path, currentpath_map)

    entry_text_map.set(map_path)


def beginparse():
    global arxml_path
    global xquery_path
    global map_path
    if var_mapflag.get():
        if (len(arxml_path) == 0) or (len(xquery_path) == 0) or (len(map_path) == 0):
            msgbox.showerror('路径错误', '请确认Arxml和XQuery路径是否正确或者勾选索引地址后未选择Map文件')
        else:
            Run_Bat()
            time.sleep(2)
            Convert_xml_to_Dict('output.xml')
            time.sleep(1)
            Save_To_Excel(Total_Dict)
            msgbox.showinfo('Success', '解析成功，请在该软件目录下查看输出文件')
    else:
        if (len(arxml_path) == 0) or (len(xquery_path) == 0):
            msgbox.showerror('路径错误', '请确认Arxml和XQuery路径是否正确')
        else:
            Run_Bat()
            time.sleep(2)
            Convert_xml_to_Dict('output.xml')
            time.sleep(1)
            Save_To_Excel(Total_Dict)
            msgbox.showinfo('Success', '解析成功，请在该软件目录下查看输出文件')


"""*******************************GUI初始化设置*******************************************"""

window = tkinter.Tk()
# 设置窗口title
window.title('Arxml Parser by Vitesco E EN BTC BSA CN CC3')
window.iconbitmap('icon.ico')
# 设置窗口大小
max_w, max_h = window.maxsize()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x = int(screen_width / 2 - 500 / 2)
y = int(screen_height / 2 - 300 / 2)
size = '{}x{}+{}+{}'.format(500, 300, x, y)
window.geometry(size)
window.resizable(width=False, height=False)

"""*******************************选择Arxml*******************************************"""

label = tkinter.Label(window, text='选择Arxml文件:', font=('宋体', 10))
label.place(x=50, y=100)
entry_text_arxml = tkinter.StringVar()
entry = tkinter.Entry(window, textvariable=entry_text_arxml, font=('宋体', 10), width=30, state='readonly')
entry.place(x=150, y=105)
button_arxml = tkinter.Button(window, text='选择路径', command=get_path_arxml)
button_arxml.place(x=400, y=95)

"""*******************************选择XQuery*******************************************"""

label = tkinter.Label(window, text='选择XQuery文件:', font=('宋体', 9))
label.place(x=50, y=150)
entry_text_xquery = tkinter.StringVar()
entry = tkinter.Entry(window, textvariable=entry_text_xquery, font=('宋体', 10), width=30, state='readonly')
entry.place(x=150, y=155)
button_xquery = tkinter.Button(window, text='选择路径', command=get_path_xquery)
button_xquery.place(x=400, y=145)

"""*******************************选择MAP*******************************************"""

label = tkinter.Label(window, text='选择Map文件:', font=('宋体', 10))
label.place(x=50, y=200)
entry_text_map = tkinter.StringVar()
entry = tkinter.Entry(window, textvariable=entry_text_map, font=('宋体', 10), width=30, state='readonly')
entry.place(x=150, y=205)

button_map = tkinter.Button(window, text='选择路径', command=index_address)
button_map.place(x=400, y=195)

"""*******************************开始解析按钮*******************************************"""

button = Button(window, text='开始解析', command=beginparse, font="宋体")
button.pack()

"""*******************************勾选map复选框*******************************************"""

var_mapflag = tkinter.BooleanVar()
checkBtnA = Checkbutton(window, text='需要索引Lif地址(勾选后需要选取map文件！)', font="宋体", variable=var_mapflag)
checkBtnA.pack()

# 显示主窗口
window.mainloop()
