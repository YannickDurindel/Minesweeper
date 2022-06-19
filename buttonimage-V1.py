from tkinter import *
from PIL import Image

def my_command():
   text.config(text= "You have clicked Me...")

win= Toplevel()
win.title("Rounded Button")
win.geometry("300x300")
"""
image = Image.open("case.png")
print(image.size)
resized_image = image.resize(50,50)
"""
click_btn= PhotoImage(file='case.png')
img_label= Label(image=click_btn)
button= Button(win, image=click_btn,command= my_command,borderwidth=0)
button.pack(pady=30)
text= Label(win, text= "")
text.pack(pady=30)
win.mainloop()