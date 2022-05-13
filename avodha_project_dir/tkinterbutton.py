from tkinter import *
root=Tk()
f=Frame(root)
f.pack()
def fun():
    print("you are logged in")
def click():
    print("successfully submitted")
Button(f,text="login",bg="cyan",command=fun).pack()
Button(f,text="submit",bg="yellow",command=click).pack()
root.mainloop()