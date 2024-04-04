from tkinter import *

window = Tk()
window.geometry("375x412")
window.title('Calculator App')
window.config(bg='black')

figures_text = StringVar()

figures_frame = Frame(window, width=375, height=500)
figures_frame.pack(side=TOP)

figures = Entry(figures_frame, width=100, textvariable=figures_text, justify=RIGHT, bg="#000", fg="white", font=('arial', 21, 'bold'))
figures.pack(ipady=20)

window.mainloop()
