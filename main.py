from tkinter import *
from ttkthemes import ThemedTk

def button_click(number):
    current = figures.get()
    figures.delete(0, END)
    figures.insert(0, str(current) + str(number))

window = ThemedTk(theme="equilux")
window.geometry("375x412")
window.title('Calculator App')
window.config(bg='black')

figures_text = StringVar()

figures_frame = Frame(window, width=375, height=500)
figures_frame.pack(side=TOP)

figures = Entry(figures_frame, width=100, textvariable=figures_text, justify=RIGHT, bg="#000", fg="white", font=('arial', 21, 'bold'))
figures.pack(ipady=20)
figures.configure(insertontime=500, insertofftime=500)
figures.configure(insertbackground="blue")  # Set cursor color to blue

# Create buttons
button_1 = Button(window, text="1", padx=40, pady=20, command=lambda: button_click(1))
button_2 = Button(window, text="2", padx=40, pady=20, command=lambda: button_click(2))
button_3 = Button(window, text="3", padx=40, pady=20, command=lambda: button_click(3))
# Add more buttons for other numbers and operations

# Place buttons on the window
button_1.pack()
button_2.pack()
button_3.pack()
# Pack more buttons accordingly

window.mainloop()
