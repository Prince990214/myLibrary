
"""
@Time ： 2023-04-11 10:22
@Auth ： Wang Zi
@File ：main
@IDE ：PyCharm
"""
import time

import pyautogui
import tkinter
import sys
from tkinter import filedialog
from tkinter import *

SleepFlag = 1
abc = 0
after_id_nosleep = None
after_id_sleep = None

def nosleep():
    global SleepFlag
    global after_id_nosleep
    SleepFlag = 1
    if SleepFlag == 1:
        # pyautogui.moveTo(400,400)
        # pyautogui.click()
        # pyautogui.moveTo(800,800)
        # pyautogui.click()
        pyautogui.press('capslock')
        after_id_nosleep = window.after(1000, nosleep)

def sleep():
    global SleepFlag
    global after_id_sleep
    global after_id_nosleep
    SleepFlag = 0
    window.after_cancel(after_id_nosleep)

"""*******************************GUI初始化设置*******************************************"""

window = tkinter.Tk()
# 设置窗口title
window.title('SlpCtr')
window.iconbitmap('icon.ico')
# 设置窗口大小
max_w, max_h = window.maxsize()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
x = int(screen_width / 2 - 500 / 2)
y = int(screen_height / 2 - 300 / 2)
size = '{}x{}+{}+{}'.format(240, 30, x, y)
window.geometry(size)
window.resizable(width=False, height=False)

"""*******************************防止休眠*******************************************"""

button1 = Button(window, text='NoSleep', command=nosleep, font="宋体")
button1.pack()
button1.place(x=50,y=0)
button1.config(fg="green")
"""*******************************结束防止休眠*******************************************"""

button2 = Button(window, text='Sleep', command=sleep, font="宋体")
button2.pack()
button2.place(x=120,y=0)
button2.config(fg="orange")

# 显示主窗口
window.mainloop()