# !/usr/bin/python3
#from tkinter import *

from tkinter import messagebox,Tk,Canvas

top = Tk()

C = Canvas(top, bg = "black", height = 250, width = 300)

coord = 10, 50, 240, 210
arc = C.create_arc(coord, start = 0, extent = 300, fill = "yellow")
line = C.create_line(10,10,200,200,fill = 'white')
C.pack()
top.mainloop()