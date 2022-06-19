from tkinter import *
from PIL import Image

def my_command():
   img.config()

win= Toplevel()
win.title("Rounded Button")
win.geometry("300x300")
click_btn= PhotoImage(file='case.png')
img_label= Label(image=click_btn)
button= Button(win, image=click_btn,command= my_command,borderwidth=0)
button.pack(pady=30)
img= Label(win, PhotoImage(file='1.png'))
img.pack(pady=30)
win.mainloop()