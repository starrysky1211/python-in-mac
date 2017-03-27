# -*- coding:utf-8 -*-

from Tkinter import *
import time


def print_time():
    nt = time.CLOCK_REALTIME
    print(nt)

print_time()
root = Tk()
root.mainloop()
