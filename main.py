from tkinter import *

def button_1_click_response():
    button_click_response('1')

def button_2_click_response():
    button_click_response('2')

def button_3_click_response():
    button_click_response('3')

def button_4_click_response():
    button_click_response('4')

def button_5_click_response():
    button_click_response('5')

def button_6_click_response():
    button_click_response('6')

def button_7_click_response():
    button_click_response('7')

def button_8_click_response():
    button_click_response('8')

def button_9_click_response():
    button_click_response('9')

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

button_4 = Button(window, text="4", command=button_4_click_response)
button_4.pack()

button_5 = Button(window, text="5", command=button_5_click_response)
button_5.pack()

window.mainloop()