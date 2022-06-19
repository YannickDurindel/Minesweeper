import tkinter as tk
"""
class Example(tk.Tk):
    def __init__(self):
        super().__init__()
        canvas = tk.Canvas(self)
        canvas.pack()
        self.startGame = tk.Button(canvas, text="Start", background='white', font=("Helvetica"))
        self.startGame.place(x=150, y=100)
        self.startGame.bind('<Button-1>', self.hide_me)

    def hide_me(self, event):
        print('hide me')
        event.widget.place_forget()

if __name__ == "__main__":
    Example().mainloop()
    """

def hide_me(self, event):
        print('hide me')
        event.widget.place_forget()

def __init__(self):
    click_btn= PhotoImage(file='case.png')
    img_label= Label(image=click_btn)
    for x in range(0,10):
        for y in range(0,10):
            button1= tk.Button(win, image=click_btn,borderwidth=0)
            button1.grid(column=x, row=y)
            button1.bind('<Button-1>', self.hide_me)
