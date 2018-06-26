from tkinter import *
from tkinter.ttk import *
from random import *

window = Tk()
window.title('Calculator')

screen = Text(window, height = 3, width = 35, borderwidth = 5, relief = 'groove')



def number1():
    print('1')
    screen.insert(INSERT, '1')
    inputs.insert(INSERT, 1)

def clear():
    screen.delete(FRONT)
    inputs.delete(0, END)

def addition():
    print('+')
    screen.insert(INSERT, '+')
    inputs.insert(INSERT, '+')

def subtraction():
    print('-')
    screen.insert(INSERT, '-')
    inputs.insert(INSERT, '*')

def division():
    print('/')
    screen.insert(INSERT, '/')
    inputs.insert(INSERT, '/')

def multiplication():
    print('*')
    screen.insert(INSERT, '*')
    inputs.insert(INSERT, '*')

def equal():
    print('=')
    answer = inputs.get()
    print(answer)
    screen.insert(INSERT, '\n')
    screen.insert(INSERT, answer)
    
def number2():
    print('2')

inputs = Entry(window)

calc1 = Button(window, text = '1', command = number1)
calc2 = Button(window, text = '2', command = number1)
calc3 = Button(window, text = '3', command = number1)
calc4 = Button(window, text = '4', command = number1)
calc5 = Button(window, text = '5', command = number1)
calc6 = Button(window, text = '6', command = number1)
calc7 = Button(window, text = '7', command = number1)
calc8 = Button(window, text = '8', command = number1)
calc9 = Button(window, text = '9', command = number1)
calc0 = Button(window, text = '0', command = number1)

equals = Button(window, text = '=', command = equal)
plus = Button(window, text = '+', command = addition)
minus = Button(window, text = '-', command = subtraction)
divide = Button(window, text = '/', command = division)
times = Button(window, text = '*', command = multiplication)
C = Button(window, text = 'C', command = clear)

screen.grid(row = 0, column = 0, columnspan = 5)

plus.grid(row = 2, column = 3)
minus.grid(row = 3, column = 3)
times.grid(row = 4, column = 3)
divide.grid(row = 5, column = 2)
equals.grid(row = 5, column = 3)
C.grid(row = 5, column = 0)


calc1.grid(row = 2, column = 0)
calc2.grid(row = 2, column = 1)
calc3.grid(row = 2, column = 2)
calc4.grid(row = 3, column = 0)
calc5.grid(row = 3, column = 1)
calc6.grid(row = 3, column = 2)
calc7.grid(row = 4, column = 0)
calc8.grid(row = 4, column = 1)
calc9.grid(row = 4, column = 2)
calc0.grid(row = 5, column = 1)


window.mainloop()
