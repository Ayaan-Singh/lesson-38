from tkinter import *
from tkinter import messagebox
root = Tk()
root.geometry('300x300')
def msg():
     messagebox.showwarning("virus detected","RIP")
button = Button(root, text="scan",command=msg)
button.place (x=40,y=40)
root.mainloop()