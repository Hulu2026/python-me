import time
from tkinter import *
tk = Tk()
canvas = Canvas(tk, width=400, height=400)
canvas.pack()
mytriangle = canvas.create_polygon(10, 10, 10, 60, 50, 35, fill='red')
canvas.itemconfig(mytriangle, fill='blue')
canvas.itemconfig(mytriangle, outline='red')
def movetriangle(event):
    if event.keysym == 'Up':
        canvas.move(mytriangle, 0, -3)
    elif event.keysym == 'Down':
        canvas.move(mytriangle, 0, 3)
    elif event.keysym == 'Left':
        canvas.move(mytriangle, -3, 0)
    else:
        canvas.move(mytriangle, 3, 0)
canvas.bind_all('<KeyPress-Up>', movetriangle)
canvas.bind_all('<KeyPress-Down>', movetriangle)
canvas.bind_all('<KeyPress-Left>', movetriangle)
canvas.bind_all('<KeyPress-Right>', movetriangle)
