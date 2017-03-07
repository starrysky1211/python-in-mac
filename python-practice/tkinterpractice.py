# -*- coding:utf-8 -*-
import sys
from tkinter import *
import time

def gettime():
    global time1
    time2 = time.strftime('%H:%M:%S')
    if (time1 != time2):
        time1 = time2
        clock.config(text = time1)
    clock.after(200,gettime)

root = Tk()
time1 = ' '
clock = Label(root,
        font = ('times' ,20 ,'bold'),
        bg = 'blue')
clock.grid(row = 0, column = 1)
gettime()

root.mainloop()

