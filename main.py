from tkinter import *

from tkinter import Menu

window = Tk()

# Title of the window
window.title("Pelataan Yatzya!")
# Default size of the window
window.geometry('2000x1000')

# Logo of the game on a canvas
canvas = Canvas(window, width=1200, height=630)
canvas.pack()
img = PhotoImage(file="yatzy-logo.png")
canvas.create_image(20,20, anchor=NW, image=img)

# Game start button
button1 = Button(window, text="Aloita peli")
button1.place(x=600, y=1500)
button1_window = canvas.create_window(600, 600, anchor=NW, window=button1)


window.mainloop()