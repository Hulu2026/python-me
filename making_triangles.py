from tkinter import *
tk = Tk()
canvas = Canvas(tk, width=400, height=400)
canvas.pack()
import random
color_list = ['red', 'blue', 'yellow', 'grey', 'pink', 'green', 'purple', 'orange']
for x in range(0, 100):
    canvas.create_polygon(random.randint(0, 400), random.randint(0, 400), random.randint(0, 400), random.randint(0, 400),  random.randint(0, 400),  random.randint(0, 400), fill=random.choice(color_list), outline='black')
