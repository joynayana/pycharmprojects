from tkinter import *
root=Tk()
root.title("radio button")
r=IntVar()
# setting value to a table
# r.set("2")

def click():
    l1['text']= r.get()
    l1.pack()

Radiobutton(root,text="option 1",variable=r,value=1).pack()
Radiobutton(root,text="option 2",variable=r,value=2).pack()
l1=Label(root,text="")
Button(root,text="click me",command=click).pack()

root.mainloop()