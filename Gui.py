from tkinter import Tk,Entry,Button,Label

Win=Tk()
Win.geometry("300x300")
txt=Entry(Win, width=10)
txt.place(x=150,y=150)
def hi():
    label=Label(Win,text=txt.get())
    label.place(x=100, y=0)

a=Button(Win, text='Hola',command=hi)
a.place(x=100, y=100)
def bye():
    label1=Label(Win,text='bye')
    label1.place(x=150, y=0)
b=Button(Win, text='Bye',command=bye)
b.place(x=150, y=100)
Win.mainloop()
print('hola mundo')
