from tkinter import *

win=Tk()
win.geometry('250x150')
r=IntVar()
R1=Checkbutton(win,text="java")
R2=Checkbutton(win,text="c++")
R3=Checkbutton(win,text="python")
R1.pack()
R2.pack()
R3.pack()
win.mainloop()
