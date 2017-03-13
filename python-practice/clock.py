# -*- coding:utf-8 -*-

from tkinter import *
import time


def get_time():

    global time1
    time2 = time.strftime('%H:%M:%S')
    if time2 != time1:
        time1 = time2
        clock.config(text=time1)
    clock.after(200, get_time)


root = Tk()
time1 = ' '
clock = Label(root,
              font=('times', 20, 'bold'),
              bg='blue')
clock.grid(row=0, column=1)
get_time()

root.mainloop()
