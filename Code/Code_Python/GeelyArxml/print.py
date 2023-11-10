"""
@Time ： 2023/10/18 12:14
@Auth ： Wang Zi
@File ：print
@IDE ：PyCharm
"""
import xml.etree.ElementTree as ET
import re
import os
import sys
import mmap
# 解析ARXML文件
file_path = ''
all_uint_clinum = []
line_array = []
short_name = []
uuid_array = []
spacecount_array = []
finaoutput_array = []
finall_array = []
filename_array = []
outputfilename_array = []
# 打包命令  pyinstaller --onefile print.py
# tree = ET.parse(file_path)
# root = tree.getroot()


# print(r"\\")
# with open('pathfile.txt', 'r') as pathfile:
#     path = pathfile.read()
#
# for file_name in os.listdir(path):
#     filename_array.append(path + file_name)
#     outputfilename_array.append(file_name.replace('arxml','txt'))
# print(outputfilename_array)
# print(filename_array)

# 查找所有标签名为SHORT-NAME的元素
def find_short_names(node, path):

    for child in node:
        if 'SHORT-NAME' in child.tag:
            # print('路径:', path, '内容:', child.text)

            # parent = child.getparent()
            # print(parent.text)

            # print(child.text)
            short_name.append(child.text)
            # print(node.findtext("UUID"))
        find_short_names(child, path + '/' + child.tag)




def UUID_Match():
    checklist = []
    temparr = []
    temp_line_arr = []
    i = 0
    colnum = 0

    # with open(file_path, 'r') as file:
    while i < len(short_name):
        # 判断第几次搜索
        count = checklist.count(short_name[i])
        checklist.append(short_name[i])

        if checklist.count(short_name[i]) > 1:
            line_array.append(temp_line_arr[checklist.index(short_name[i])][checklist.count(short_name[i]) - 1])
            temp_line_arr.append(1)
            # temparr.append(line_number)
            temparr = []
            i = i + 1
        else:
            with open(file_path, 'r') as file:
                for line_number, line in enumerate(file, 1):
                    if "<SHORT-NAME>" + short_name[i] + "</SHORT-NAME>" in line:
                        # print("<SHORT-NAME>" + nameArray[i] + "</SHORT-NAME>")
                        # print(f"找到字符串 '{nameArray[i]}' 在第 {line_number} 行：{line}")
                        temparr.append(line_number)
                        # all_uint_clinum.append(temparr)
                        # temparr = []
                # print(temparr)
                # print(short_name[i])
                # print(temparr[count])
                line_array.append(temparr[count])
                temp_line_arr.append(temparr)
                temparr = []
                i = i + 1



def zhengzezousuoandprint():
    c = 0
    match_num = 0
    # print(len(short_name))
    # print(len(line_array))
    # with open(file_path, 'r') as file:
    #     lines = file.readlines()
    while c < len(line_array):
        with open(file_path, 'r') as file:
            lines = file.readlines()

            spacecal = lines[line_array[c] - 1].count("  ")
            spacecount_array.append(spacecal)

            specific_line = lines[line_array[c] - 2]
            matches = re.findall(r'"([^"]*)"', specific_line)
            # print(specific_line)
            for match in matches:
                uuid_array.append(match)
                match_num = match_num + 1
            if match_num == 0:
                uuid_array.append("none")
            match_num = 0
            c = c + 1
    # print(spacecount_array)
    # print(len(spacecount_array))
    cc = 0
    while cc < len(line_array):
        finaoutput_array.append(uuid_array[cc] + ";" + short_name[cc])
        # print(uuid_array[cc] + ";" + short_name[cc])
        cc = cc + 1
    # print(finaoutput_array[15])


def pathdef():
    i = 0
    j = 1
    temppatharray = []
    strpath = ""
    maxvalue = max(spacecount_array)
    minvalue = min(spacecount_array)
    while i < len(spacecount_array):
        if spacecount_array[i] == minvalue:
            finall_array.append(uuid_array[i] + ";" + short_name[i])
        elif minvalue < spacecount_array[i] <= maxvalue:
            tempspacecount = spacecount_array[i]
            while i >= 0:
                while tempspacecount <= spacecount_array[i - j]:
                    if i - j == 0:
                        break
                    else:
                        j = j + 1
                if tempspacecount > minvalue:

                    tempspacecount = spacecount_array[i - j]

                else:
                    break

                strpath = "/" + short_name[i - j] + strpath
                temppatharray.append("/" + short_name[i - j])
            j = 1
            strpath = strpath
            finall_array.append(uuid_array[i] + ";" + strpath + "/" + short_name[i])
            strpath = ""

        i = i + 1
    # print(finall_array)


def output():
    index = 0
    while index < len(finall_array):
        if "/Element" not in finall_array[index]:
            print(finall_array[index])
        index = index + 1


    # print(len(finall_array))
# find_short_names(root, root.tag)
# UUID_Match()
# zhengzezousuoandprint()
# pathdef()



if __name__ == '__main__':

    file_path = sys.argv[1]
    # file_path = 'D:\casdev\CanSigMonr.arxml'
    # print(file_path)
    tree = ET.parse(file_path)
    root = tree.getroot()
    find_short_names(root, root.tag)
    UUID_Match()
    zhengzezousuoandprint()
    pathdef()
    output()
    all_uint_clinum = []
    line_array = []
    short_name = []
    uuid_array = []
    spacecount_array = []
    finaoutput_array = []
    finall_array = []
    # i = i + 1
