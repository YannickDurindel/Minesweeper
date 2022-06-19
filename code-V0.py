import random
from tkinter import *

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
for i in range(0,5):
    row=random.randint(0,9)
    column=random.randint(0,9)
    matrix[row][column]=1

root=Tk()
root.title('démineur')
button = Button(root, image='case.png',foreground='#FFFFFF',background="#74bbe4", padx="369", pady="30")
button.grid(column=0, row=1)
root.mainloop()