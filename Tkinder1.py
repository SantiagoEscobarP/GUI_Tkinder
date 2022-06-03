# !/usr/bin/python3
import serial
import time

com_serial=serial.Serial('COM2',9600, timeout=0)
from tkinter import Tk,Label,Button


top = Tk()
top.geometry("200x200")
def helloCallBack():
    com_serial.readline()
    import matplotlib.pyplot as plt
    plt.plot([1, 2, 3, 4, 5],[4,8,13,17,20])
    com_serial.write(b'recibido\n\r')
    plt.show()
    com_serial.write(b'recibido\n\r')
    
def byecallBack():
    a=com_serial.readline()
    print(a)
    label = Label(top, text=a)
    label.grid(row = 0, column = 0, pady = 100, padx = 80)
    com_serial.write(b'recibido\n\r')
B = Button(top, text = "Hello", command = helloCallBack)
B.place(x = 50,y = 0)
c = Button(top, text = "bye", command = byecallBack)
c.place(x = 150,y = 0)
top.mainloop()