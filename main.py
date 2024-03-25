from tkinter import *
def button_1_click_response():
    button_click_response('1')

def button_2_click_response():
    button_click_response('2')

def button_3_click_response():
    button_click_response('3')

def button_4_click_response():
    button_click_response('4')

def button_click_response(char):
    figures.insert(END, char)


window = Tk()
window.minsize(width=500, height=500)
window.title('Calculator App')

figures = Entry(width=50)
figures.pack()

button_1 = Button(window, text="1", command=button_1_click_response)
button_1.pack()

button_2 = Button(window, text="2", command=button_2_click_response)
button_2.pack()

button_3 = Button(window, text="3", command=button_3_click_response)
button_3.pack()

window.mainloop()