from tkinter import *

def clear():
    figures.delete(0, END)


window = Tk()
window.geometry("312x324")
window.title('Calculator App')

figures = Entry(window, width=50)
figures.grid(row=)

button_clear = Button(window, text="Clear", command=clear)
button_clear.pack()

window.mainloop()