from tkinter import *
root=Tk()
root.title("tkinter slider")
root.geometry('400x400')
def click():
    l1['text']=hori.get()
    root.geometry(str(hori.get())+'x400')
# vertical slider
ver=Scale(root,from_=0,to=200)
ver.pack()
# horizontal slider
hori=Scale(root,from_=0,to=200,orient=HORIZONTAL)
hori.pack()
l1=Label(root,text=hori.get(),bg="red")
l1.pack()
Button(root,text="click",command=click).pack()

root.mainloop()