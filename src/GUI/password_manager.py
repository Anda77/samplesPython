from tkinter import *

window = Tk()
window.title("Password Manager App")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)

photo_image = PhotoImage(file="C:\\PythonPrj\\resources\\logo.png")

canvas.create_image(100, 100, image=photo_image)
canvas.pack()

window.mainloop()
