from tkinter import *


window = Tk()
window.geometry("312x324")
window.title('Calculator App')
window.config(bg='black')
figures_frame= Frame(window, width=312, height=80,  )
figures_frame.pack(side=TOP)
figures = Entry(figures_frame, width=50)
figures.grid(row=0, column=0, columnspan=4)



window.mainloop()
