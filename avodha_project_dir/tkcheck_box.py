from tkinter import *
root=Tk()
root.title("checkbutton")
root.geometry('500x500')
# checkbutton creating
abc=IntVar()
aef=StringVar()
def check1():
    mylabel=Label(root,text=abc.get()).grid(row=0,column=2)
def check2():
    label2=Label(root,text=aef.get()).grid(row=1,column=3)
# first check button of int
c1=Checkbutton(root,text="Agree terms and condition",fg="brown",variable=abc,onvalue=1,offvalue=0)
c1.grid(row=0,column=0)
# second check button of strings
c2=Checkbutton(root,text="are you sure",fg="brown",variable=aef,onvalue='true',offvalue='false')
# used to avoid select first run
c2.deselect()
c2.grid(row=1,column=0)
# button b1 for check current value
b1=Button(root,text="click here",command=check1)
b1.grid(row=0,column=1)
# button b2 for checking current value
b2=Button(root,text="2nd one",command=check2)
b2.grid(row=1,column=1)

root.mainloop()