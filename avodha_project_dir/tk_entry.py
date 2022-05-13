from tkinter import *
root=Tk()
root.geometry('300x400')
l1=Label(root,text="enter you name:",bg="yellow")
l1.grid(row=0,column=0)
e1=Entry(root,justify='center')
e1.insert(END,"enter your text here")
e1.grid(row=0,column=1)
root.mainloop()
