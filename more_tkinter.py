from tkinter import *
tk = Tk()
canvas = Canvas(tk, width=400, height=400)
canvas.pack()
canvas.create_text(150, 100, text='There was once a man from Tolouse,')
canvas.create_text(130, 120, text='Who rode around on a moose.', fill="red")
canvas.create_text(150, 150, text='He said, It\'s my curse,', font=('Times', 15))
canvas.create_text(200, 200, text='But it could be worse,', font=('Helvectica', 20))
canvas.create_text(220, 250, text='My cousin rides round', font=('Courier', 22))
canvas.create_text(220, 300, text='on a goose.', font=('Courier', 30))
