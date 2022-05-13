from tkinter import *
root=Tk()
class demo:
    def __init__(self,rootone):
        f=Frame(rootone)
        f.pack()
        self.p=Button(f,text="CLICK",fg="red",bg="yellow",command=self.printMsg)
        self.p.pack()
        Button(f,text="EXIT",fg="red",bg="yellow",command=f.quit).pack()
    def printMsg(self):
        print("Hi Welcome to new world..")
obj=demo(root)
root.mainloop()

