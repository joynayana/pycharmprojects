from tkinter import *
from tkinter import ttk
# create instance tkinter frame
root=Tk()
def data():
    Label(root,text=combo1.get()).grid(row=1,column=1)

# creating first combobox
combo1=ttk.Combobox()
combo1['values']=(1,2,3,4,5,"text")
combo1.current(3)
combo1.grid(row=0,column=0)

#creating second combobox
combo2=ttk.Combobox()
t1=('nayana','alvin','jack','kunju')
combo2['values']=t1
combo2.grid(row=0,column=1)
Button(root,text="click here",command=data).grid(row=1,column=0)
root.mainloop()