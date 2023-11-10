"""
@Time ： 2023/10/12 9:18
@Auth ： Wang Zi
@File ：Write
@IDE ：PyCharm
"""
import xlrd

content = ""
rx = 36
tx = 33
MessageName = [
"BecmPropFr01",
"BecmPropFr02",
"BecmPropFr03",
"BecmPropFr04",
"BecmPropFr05",
"BecmPropFr07",
"BecmPropFr08",
"BecmPropFr09",
"BecmPropFr11",
"BecmPropFr12",
"BecmPropFr13",
"BecmPropFr14",
"BecmPropFr15",
"BecmPropFr16",
"BecmPropFr17",
"BecmPropFr18",
"BecmPropFr19",
"BecmPropFr20",
"BecmPropFr21",
"BecmPropFr22",
"BecmPropFr23",
"BecmPropFr24",
"BecmPropFr27",
"BecmPropFr28",
"BecmPropFr30",
"BecmPropFr31",
"BecmPropFr32",
"BecmPropFr34",
"BecmPropFr40",
"BecmPropNMFr",
"BecmPropVFCVectorFr",
"BecmToDhuJ1979OBDPropDiagResFram11",
"BecmToVddmPropDiagResFrame",
"CddIgmPropFr01",
"CddIgmPropFr02",
"CddObcPropFr01",
"CddObcPropFr02",
"CddObcPropFr03",
"CddPropNmFr12",
"EcmPropFr02",
"EcmPropFr04",
"EcmPropFr05",
"EcmPropFr08",
"EcmPropFr09",
"EcmPropFr11",
"EcmPropFr22",
"EcmPropFr24",
"EcmPropFr25",
"EcmPropFr29",
"EcmPropXEVFr16",
"IgmMgmPropFr03",
"IgmMgmPropFr05",
"IgmMgmPropFr06",
"SrsPropFr02",
"TcmPropFr04",
"VcuPropFr05",
"VddmPropFr05",
"VddmPropFr06",
"VddmPropFr11",
"VddmPropFr15",
"VddmPropFr17",
"VddmPropFr18",
"VddmPropFr19",
"VddmPropFr26",
"VddmPropFr31",
"VddmPropFr36",
"VddmPropFr37",
"VddmPropFr38",
"VddmPropFr45"

]
TxName = [
"BecmPropFr01",
"BecmPropFr02",
"BecmPropFr03",
"BecmPropFr04",
"BecmPropFr05",
"BecmPropFr07",
"BecmPropFr08",
"BecmPropFr09",
"BecmPropFr11",
"BecmPropFr12",
"BecmPropFr13",
"BecmPropFr14",
"BecmPropFr15",
"BecmPropFr16",
"BecmPropFr17",
"BecmPropFr18",
"BecmPropFr19",
"BecmPropFr20",
"BecmPropFr21",
"BecmPropFr22",
"BecmPropFr23",
"BecmPropFr24",
"BecmPropFr27",
"BecmPropFr28",
"BecmPropFr30",
"BecmPropFr31",
"BecmPropFr32",
"BecmPropFr34",
"BecmPropFr40",
"BecmPropNMFr",
"BecmPropVFCVectorFr",
"BecmToDhuJ1979OBDPropDiagResFram11",
"BecmToVddmPropDiagResFrame"

]
TxCanId = [
'0x141',
'0x175',
'0x178',
'0x293',
'0x295',
'0x296',
'0x342',
'0x315',
'0x331',
'0x301',
'0x298',
'0x286',
'0x143',
'0x341',
'0x345',
'0x346',
'0x347',
'0x145',
'0x288',
'0x53',
'0x142',
'0x290',
'0x499',
'0x49C',
'0x478',
'0x140',
'0x182',
'0x17B',
'0x183',
'0x519',
'0x559',
'0x7EA',
'0x635'

]
RxName = [
"CddIgmPropFr01",
"CddIgmPropFr02",
"CddObcPropFr01",
"CddObcPropFr02",
"CddObcPropFr03",
"CddPropNmFr12",
"EcmPropFr02",
"EcmPropFr04",
"EcmPropFr05",
"EcmPropFr08",
"EcmPropFr09",
"EcmPropFr11",
"EcmPropFr22",
"EcmPropFr24",
"EcmPropFr25",
"EcmPropFr29",
"EcmPropXEVFr16",
"IgmMgmPropFr03",
"IgmMgmPropFr05",
"IgmMgmPropFr06",
"SrsPropFr02",
"TcmPropFr04",
"VcuPropFr05",
"VddmPropFr05",
"VddmPropFr06",
"VddmPropFr11",
"VddmPropFr15",
"VddmPropFr17",
"VddmPropFr18",
"VddmPropFr19",
"VddmPropFr26",
"VddmPropFr31",
"VddmPropFr36",
"VddmPropFr37",
"VddmPropFr38",
"VddmPropFr45"

]
RxCanId = [
'0x14B',
'0x149',
'0x218',
'0x216',
'0x12A',
'0x103',
'0x66',
'0x131',
'0x84',
'0x171',
'0x196',
'0x287',
'0x188',
'0x4B',
'0x27A',
'0x116',
'0x289',
'0x13A',
'0x156',
'0x95',
'0x35',
'0x181',
'0x151',
'0x76',
'0x235',
'0x139',
'0x261',
'0x162',
'0x56',
'0x285',
'0x236',
'0x41B',
'0x477',
'0x177',
'0x333',
'0x117'

]
SignalArray = []
RxRefNum = []
TxRefNum = []
TxCanIdd = [
0x141,
0x175,
0x178,
0x293,
0x295,
0x296,
0x342,
0x315,
0x331,
0x301,
0x298,
0x286,
0x143,
0x341,
0x345,
0x346,
0x347,
0x145,
0x288,
0x53,
0x142,
0x290,
0x499,
0x49C,
0x478,
0x140,
0x182,
0x17B,
0x183,
0x519,
0x559,
0x7EA,
0x635

]

zhichao = [
"SPN3201_BMV_CellVoltageAry1",
"SPN3102_BMV_CellVoltageAry2",
"SPN3103_BMV_CellVoltageAry3",
"SPN3104_BMV_CellVoltageAry4",
"SPN3105_BMV_CellVoltageAry5",
"SPN3106_BMV_CellVoltageAry6",
"SPN3107_BMV_CellVoltageAry7",
"SPN3108_BMV_CellVoltageAry8",
"SPN3109_BMV_CellVoltageAry9",
"SPN3110_BMV_CellVoltageAry10",
"SPN3111_BMV_CellVoltageAry11",
"SPN3112_BMV_CellVoltageAry12",
"SPN3113_BMV_CellVoltageAry13",
"SPN3114_BMV_CellVoltageAry14",
"SPN3115_BMV_CellVoltageAry15",
"SPN3116_BMV_CellVoltageAry16",
"SPN3117_BMV_CellVoltageAry17",
"SPN3118_BMV_CellVoltageAry18",
"SPN3119_BMV_CellVoltageAry19",
"SPN3120_BMV_CellVoltageAry20",
"SPN3121_BMV_CellVoltageAry21",
"SPN3122_BMV_CellVoltageAry22",
"SPN3123_BMV_CellVoltageAry23",
"SPN3124_BMV_CellVoltageAry24",
"SPN3125_BMV_CellVoltageAry25",
"SPN3126_BMV_CellVoltageAry26",
"SPN3127_BMV_CellVoltageAry27",
"SPN3128_BMV_CellVoltageAry28",
"SPN3129_BMV_CellVoltageAry29",
"SPN3130_BMV_CellVoltageAry30",
"SPN3131_BMV_CellVoltageAry31",
"SPN3132_BMV_CellVoltageAry32",
"SPN3133_BMV_CellVoltageAry33",
"SPN3134_BMV_CellVoltageAry34",
"SPN3135_BMV_CellVoltageAry35",
"SPN3136_BMV_CellVoltageAry36",
"SPN3137_BMV_CellVoltageAry37",
"SPN3138_BMV_CellVoltageAry38",
"SPN3139_BMV_CellVoltageAry39",
"SPN3140_BMV_CellVoltageAry40",
"SPN3141_BMV_CellVoltageAry41",
"SPN3142_BMV_CellVoltageAry42",
"SPN3143_BMV_CellVoltageAry43",
"SPN3144_BMV_CellVoltageAry44",
"SPN3145_BMV_CellVoltageAry45",
"SPN3146_BMV_CellVoltageAry46",
"SPN3147_BMV_CellVoltageAry47",
"SPN3148_BMV_CellVoltageAry48",
"SPN3149_BMV_CellVoltageAry49",
"SPN3150_BMV_CellVoltageAry50",
"SPN3151_BMV_CellVoltageAry51",
"SPN3152_BMV_CellVoltageAry52",
"SPN3153_BMV_CellVoltageAry53",
"SPN3154_BMV_CellVoltageAry54",
"SPN3155_BMV_CellVoltageAry55",
"SPN3156_BMV_CellVoltageAry56",
"SPN3157_BMV_CellVoltageAry57",
"SPN3158_BMV_CellVoltageAry58",
"SPN3159_BMV_CellVoltageAry59",
"SPN3160_BMV_CellVoltageAry60",
"SPN3161_BMV_CellVoltageAry61",
"SPN3162_BMV_CellVoltageAry62",
"SPN3163_BMV_CellVoltageAry63",
"SPN3164_BMV_CellVoltageAry64",
"SPN3165_BMV_CellVoltageAry65",
"SPN3166_BMV_CellVoltageAry66",
"SPN3167_BMV_CellVoltageAry67",
"SPN3168_BMV_CellVoltageAry68",
"SPN3169_BMV_CellVoltageAry69",
"SPN3170_BMV_CellVoltageAry70",
"SPN3171_BMV_CellVoltageAry71",
"SPN3172_BMV_CellVoltageAry72",
"SPN3173_BMV_CellVoltageAry73",
"SPN3174_BMV_CellVoltageAry74",
"SPN3175_BMV_CellVoltageAry75",
"SPN3176_BMV_CellVoltageAry76",
"SPN3177_BMV_CellVoltageAry77",
"SPN3178_BMV_CellVoltageAry78",
"SPN3179_BMV_CellVoltageAry79",
"SPN3180_BMV_CellVoltageAry80",
"SPN3181_BMV_CellVoltageAry81",
"SPN3182_BMV_CellVoltageAry82",
"SPN3183_BMV_CellVoltageAry83",
"SPN3184_BMV_CellVoltageAry84",
"SPN3185_BMV_CellVoltageAry85",
"SPN3186_BMV_CellVoltageAry86",
"SPN3187_BMV_CellVoltageAry87",
"SPN3188_BMV_CellVoltageAry88",
"SPN3189_BMV_CellVoltageAry89",
"SPN3190_BMV_CellVoltageAry90",
"SPN3191_BMV_CellVoltageAry91",
"SPN3192_BMV_CellVoltageAry92",
"SPN3193_BMV_CellVoltageAry93",
"SPN3194_BMV_CellVoltageAry94",
"SPN3195_BMV_CellVoltageAry95",
"SPN3196_BMV_CellVoltageAry96",
"SPN3197_BMV_CellVoltageAry97",
"SPN3198_BMV_CellVoltageAry98",
"SPN3199_BMV_CellVoltageAry99",
"SPN3200_BMV_CellVoltageAry100",
"SPN3201_BMV_CellVoltageAry101",
"SPN3202_BMV_CellVoltageAry102",
"SPN3203_BMV_CellVoltageAry103",
"SPN3204_BMV_CellVoltageAry104",
"SPN3205_BMV_CellVoltageAry105",
"SPN3206_BMV_CellVoltageAry106",
"SPN3207_BMV_CellVoltageAry107",
"SPN3208_BMV_CellVoltageAry108",
"SPN3209_BMV_CellVoltageAry109",
"SPN3210_BMV_CellVoltageAry110",
"SPN3211_BMV_CellVoltageAry111",
"SPN3212_BMV_CellVoltageAry112",
"SPN3213_BMV_CellVoltageAry113",
"SPN3214_BMV_CellVoltageAry114",
"SPN3215_BMV_CellVoltageAry115",
"SPN3216_BMV_CellVoltageAry116",
"SPN3217_BMV_CellVoltageAry117",
"SPN3218_BMV_CellVoltageAry118",
"SPN3219_BMV_CellVoltageAry119",
"SPN3220_BMV_CellVoltageAry120",
"SPN3221_BMV_CellVoltageAry121",
"SPN3222_BMV_CellVoltageAry122",
"SPN3223_BMV_CellVoltageAry123",
"SPN3224_BMV_CellVoltageAry124",
"SPN3225_BMV_CellVoltageAry125",
"SPN3226_BMV_CellVoltageAry126"
]
def write():
    i = 0
    with open('Write.txt', 'w') as f:
        while i < 126:
            f.write(read())
            i = i + 1

def read():
    with open('Read.txt', 'r') as f:
        content = f.read()
        print(content)
        return content

def replace():
    i = 0
    cc = 0
    while i < 126:
        with open(r'Write.txt', 'r', encoding='UTF-8') as file:
            # 使用 read() 函数读取文件内容并将它们存储在一个新变量中
            data = file.read()
            # replaced = "\"CanId\""
            replaced = "nameee"
            # if int(SignalArray[i][2]) < 9:
            #     data = data.replace(replaced, "UINT8", 1)
            # elif 8 < int(SignalArray[i][2]) < 17:
            #     data = data.replace(replaced, "UINT16", 1)
            # else :
            #     data = data.replace(replaced, "UINT32", 1)
            data = data.replace("nameee", zhichao[i],1)
            # data = data.replace(replaced, str(i + 51),1)
            i = i + 1
            cc = cc + 16
        with open(r'Write.txt', 'w', encoding='UTF-8') as file:
            # 在文本文件中写入替换的数据
            file.write(data)
    print(i)

def readdatafromxlsx():
    # 331行是最后一个发送信号
    global SignalArray
    global RxRefNum
    global TxRefNum
    i = 1
    index = 0
    num = 0
    rxnum = 0
    txnum = 0
    while i < 528:
        xlsx = xlrd.open_workbook('signal.xlsx')
        # 通过sheet名查找：xlsx.sheet_by_name("sheet1")
        xlsx.sheet_by_index(0)
        table = xlsx.sheet_by_index(0)
        text = table.cell_value(i, 0)
        split_text = text.split(";")
        SignalArray.append(split_text)
        i = i + 1
    print(SignalArray)
    print(len(SignalArray))
    temp = 0
    while temp < 527 :
        if temp < 330:
            print("SGBMS_" + str(SignalArray[temp][0]) + "_" + str(int(SignalArray[temp][4],16)) + "T")
        else:
            print("SGBMS_" + str(SignalArray[temp][0]) + "_" + str(int(SignalArray[temp][4], 16)) + "R")
        temp = temp + 1
    """
    Rx
    while rxnum < 36:

        while index < 197:
            if (SignalArray[index].count(RxCanId[rxnum])) == 1:
                num = num + 1
            index = index + 1
        print(num)
        RxRefNum.append(num)
        rxnum = rxnum + 1
        index = 0
        num = 0
    print(RxRefNum)
    Tx
    while rxnum < len(TxCanId):

        while index < 330:
            if (SignalArray[index].count(TxCanId[txnum])) == 1:
                num = num + 1
            index = index + 1
        print(num)
        TxRefNum.append(num)
        txnum = txnum + 1
        index = 0
        num = 0
    # print(TxRefNum)
    """
if __name__ == '__main__':
    # read()
    # write()
    # readdatafromxlsx()
    replace()
    # TxCanIdd.sort()
    # for i in range(len(TxCanIdd)):
    #     TxCanIdd[i] = hex(TxCanIdd[i])
    # print(TxCanIdd)
    # 
    # a = []
    # i = 0
    # # print(str(int(TxCanId[4], 16)))
    # # print(TxCanId[0](1,-1))
    # for i in range(len(TxCanId)):
    #     print(int(TxCanId[i],16))

    """
    while i < 33:

        a.append(str(int(TxCanId[i], 16)))
        i = i + 1

    # a.sort()
    print(a)
    while i < 33:

        a[i] = a[i][0:1]
        i = i + 1
    print(a)
    """
