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

def button_0_click_response():
    button_click_response('0')

def button_operation_response():
    button_click_response('0')

def button_click_response(char):
    figures.insert(END, char)

def button_add_click():
    operation_click_response("+")

def button_subtract_click():
    operation_click_response("-")

def button_divide_click():
    operation_click_response("/")

def button_multiply_click():
    operation_click_response("*")

def operation_click_response(operation):
    expression = figures.get()
    figures.delete(0, END)
    figures.insert(END, f"{expression} {operation} ")

def calculate():
    expression = figures.get()
    result = eval(expression)  
    figures.delete(0, END)
    figures.insert(END, result)

def clear():
    figures.delete(0, END)


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

button_6 = Button(window, text="6", command=button_6_click_response)
button_6.pack()

button_7 = Button(window, text="7", command=button_7_click_response)
button_7.pack()

button_8 = Button(window, text="8", command=button_8_click_response)
button_8.pack()

button_9 = Button(window, text="9", command=button_9_click_response)
button_9.pack()

button_0 = Button(window, text="0", command=button_0_click_response)
button_0.pack()

button_addition = Button(window, text="+", command=button_add_click)
button_addition.pack()

button_subtract = Button(window, text="-", command=button_subtract_click)
button_subtract.pack()

button_divide = Button(window, text="/", command=button_divide_click)
button_divide.pack()

button_multiply = Button(window, text="*", command=button_multiply_click)
button_multiply.pack()

button_answer = Button(window, text="=", command=calculate, width=20)
button_answer.pack()

button_clear = Button(window, text="Clear", command=clear)
button_clear.pack()

window.mainloop()