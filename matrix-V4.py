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

result=[[0,0,0,0,0,0,0,0,0,0],
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

for i in range(0,10):
    row=random.randint(0,9)
    column=random.randint(0,9)
    matrix[row][column]=1

win= Toplevel()
win.title("Minesweeper")
win.geometry("428x430")

for x in range(1,9):
    for y in range(1,9):
        n=0
        if matrix[x-1][y-1]==1:
            n+=1
        if matrix[x-1][y]==1:
            n+=1
        if matrix[x-1][y+1]==1:
            n+=1
        if matrix[x][y-1]==1:
            n+=1
        if matrix[x][y+1]==1:
            n+=1
        if matrix[x+1][y-1]==1:
            n+=1
        if matrix[x+1][y]==1:
            n+=1
        if matrix[x+1][y+1]==1:
            n+=1
        result[x][y]=n
    n=0
    if matrix[x-1][0]==1:
        n+=1
    if matrix[x-1][1]==1:
        n+=1
    if matrix[x][1]==1:
        n+=1
    if matrix[x+1][0]==1:
        n+=1
    if matrix[x+1][1]==1:
        n+=1
    result[x][0]=n
    n=0
    if matrix[x-1][9]==1:
        n+=1
    if matrix[x-1][8]==1:
        n+=1
    if matrix[x][8]==1:
        n+=1
    if matrix[x+1][9]==1:
        n+=1
    if matrix[x+1][8]==1:
        n+=1
    result[x][9]=n
    n=0
    if matrix[0][x-1]==1:
        n+=1
    if matrix[1][x-1]==1:
        n+=1
    if matrix[1][x]==1:
        n+=1
    if matrix[1][x+1]==1:
        n+=1
    if matrix[0][x+1]==1:
        n+=1
    result[0][x]=n
    n=0
    if matrix[9][x-1]==1:
        n+=1
    if matrix[8][x-1]==1:
        n+=1
    if matrix[8][x]==1:
        n+=1
    if matrix[8][x+1]==1:
        n+=1
    if matrix[9][x+1]==1:
        n+=1
    result[9][x]=n
n=0
if matrix[0][1]==1:
    n+=1
if matrix[1][1]==1:
    n+=1
if matrix[1][0]==1:
    n+=1
result[0][0]=n
n=0
if matrix[0][8]==1:
    n+=1
if matrix[1][8]==1:
    n+=1
if matrix[1][9]==1:
    n+=1
result[0][9]=n
n=0
if matrix[8][0]==1:
    n+=1
if matrix[8][1]==1:
    n+=1
if matrix[9][1]==1:
    n+=1
result[9][0]=n
n=0
if matrix[9][8]==1:
    n+=1
if matrix[8][8]==1:
    n+=1
if matrix[8][9]==1:
    n+=1
result[9][9]=n
for x in range(0,10):
    for y in range(0,10):
        if result[x][y]==0:
            image0 = Image.open("case.png")
            test = ImageTk.PhotoImage(image0)
            label1 = tkinter.Label(win,image=test)
            label1.image = test
            label1.grid(column=x, row=y)
            img[x][y]=image0
        if result[x][y]==1:
            image1 = Image.open("1.png")
            test = ImageTk.PhotoImage(image1)
            label1 = tkinter.Label(win,image=test)
            label1.image = test
            label1.grid(column=x, row=y)
            img[x][y]=image1
        if result[x][y]==2:
            image2 = Image.open("2.png")
            test = ImageTk.PhotoImage(image2)
            label1 = tkinter.Label(win,image=test)
            label1.image = test
            label1.grid(column=x, row=y)
            img[x][y]=image2
        if result[x][y]==3:
            image3 = Image.open("3.png")
            test = ImageTk.PhotoImage(image3)
            label1 = tkinter.Label(win,image=test)
            label1.image = test
            label1.grid(column=x, row=y)
            img[x][y]=image3
        if result[x][y]==4:
            image4 = Image.open("4.png")
            test = ImageTk.PhotoImage(image4)
            label1 = tkinter.Label(win,image=test)
            label1.image = test
            label1.grid(column=x, row=y)
            img[x][y]=image4
        if matrix[x][y]==1:
            image10 = Image.open("bomb.png")
            test = ImageTk.PhotoImage(image10)
            label1 = tkinter.Label(win,image=test)
            label1.image = test
            label1.grid(column=x, row=y)
            img[x][y]=image10



win.mainloop()