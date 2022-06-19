import tkinter
from tkinter import *
from PIL import ImageTk, Image

def my_command():
   image1 = Image.open("1.png")
   test = ImageTk.PhotoImage(image1)
   label1 = tkinter.Label(win,image=test)
   label1.image = test
   label1.grid(column=0, row=0)

win= Toplevel()
win.title("Minesweeper")
win.geometry("300x300")
click_btn= PhotoImage(file='case.png')
img_label= Label(image=click_btn)
button= Button(win, image=click_btn,command= my_command,borderwidth=0)
button.grid(column=0, row=0)
win.mainloop()