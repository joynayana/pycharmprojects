from tkinter import *
root=Tk()
def open():
  top=Toplevel()
  top.title("2nd window")
  Label(top,text="Here is the new window ,hai welcome",bg="red").pack()
  Button(top,text="goto 1st window",command=top.destroy).pack()

Button(root,text="click here to go new window",command=open).pack()
root.mainloop()
