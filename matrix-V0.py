import random
import tkinter
from tkinter import *
from PIL import Image, ImageTk

matrix=[[0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0]]

img  = [[0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0],
        [0,0,0,0,0,0,0,0,0,0]]
print(matrix)
for i in range(0,5):
    row=random.randint(0,9)
    column=random.randint(0,9)
    matrix[row][column]=1
print(matrix)
win= Toplevel()
win.title("Minesweeper")
win.geometry("375x375")

for x in range(1,9):
    for y in range(1,9):
        n=0
        if matrix[x-1][y-1]==1:
            n+=1
        elif matrix[x-1][y]==1:
            n+=1
        elif matrix[x-1][y+1]==1:
            n+=1
        elif matrix[x][y-1]==1:
            n+=1
        elif matrix[x][y+1]==1:
            n+=1
        elif matrix[x+1][y-1]==1:
            n+=1
        elif matrix[x+1][y]==1:
            n+=1
        elif matrix[x+1][y+1]==1:
            n+=1
        if n==0:
            image0 = Image.open("case.png")
            test = ImageTk.PhotoImage(image0)
            label1 = tkinter.Label(win,image=test)
            label1.image = test
            label1.grid(column=x, row=y)
            img[x][y]=image0
        elif n==1:
            image1 = Image.open("1.png")
            test = ImageTk.PhotoImage(image1)
            label1 = tkinter.Label(win,image=test)
            label1.image = test
            label1.grid(column=x, row=y)
            img[x][y]=image1
        elif n==2:
            image2 = Image.open("2.png")
            test = ImageTk.PhotoImage(image2)
            label1 = tkinter.Label(win,image=test)
            label1.image = test
            label1.grid(column=x, row=y)
            img[x][y]=image2
        elif n==3:
            image3 = Image.open("3.png")
            test = ImageTk.PhotoImage(image3)
            label1 = tkinter.Label(win,image=test)
            label1.image = test
            label1.grid(column=x, row=y)
            img[x][y]=image3
        elif n==4:
            image4 = Image.open("4.png")
            test = ImageTk.PhotoImage(image4)
            label1 = tkinter.Label(win,image=test)
            label1.image = test
            label1.grid(column=x, row=y)
            img[x][y]=image4
        elif matrix[x][y]==1:
            image10 = Image.open("bomb.png")
            test = ImageTk.PhotoImage(image10)
            label1 = tkinter.Label(win,image=test)
            label1.image = test
            label1.grid(column=x, row=y)
            img[x][y]=image10


win.mainloop()