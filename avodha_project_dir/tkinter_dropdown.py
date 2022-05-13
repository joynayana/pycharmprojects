from tkinter import *
root=Tk()
mainmenu=Menu(root)
def msg():
    print("my function")
# first menu file
submenu1=Menu(mainmenu)
mainmenu.add_cascade(label="File",menu=submenu1)
submenu1.add_command(label="Save",command=msg)
submenu1.add_separator()
submenu1.add_command(label="Exit",command=root.quit)
# second menu edit
submenu2=Menu(mainmenu)
mainmenu.add_cascade(label="Edit",menu=submenu2)
submenu2.add_command(label="Undo")
submenu2.add_command(label="Redo")
# display menubar
root.config(menu=mainmenu)
root.mainloop()