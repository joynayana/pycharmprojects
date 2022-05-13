from tkinter import *
root=Tk()
Label(root,text="User Name",bg="cyan").grid(row=0,column=0)
Label(root,text="Password",bg="cyan").grid(row=1,column=0)
# entry for data enter to textbox
Entry(root).grid(row=0,column=1)
Entry(root).grid(row=1,column=1)
root.mainloop()