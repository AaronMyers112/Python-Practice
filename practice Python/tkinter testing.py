from tkinter import *
from tkinter.ttk import Progressbar
from time import *
from random import *

window = Tk()

window.title('Test')

step_size = 5

words = [['hi', 'bye', 'are', 'you', 'okay', 'yes', 'I', 'am', 'good',
          'bad', 'ugly', 'a', 'words', 'fair', 'play', 'today', 'tomorrow',
          'yesterday', 'this week', 'next week', 'last week', 'this year',
          'next year', 'last year'],
         ['Who', 'What', 'When', 'Where', 'Why', 'How']]

letters = [['a', 'e', 'i', 'o', 'u'],
           ['b', 'c', 'd', 'f', 'g',
            'h', 'j', 'k', 'l', 'm',
            'n', 'p', 'q', 'r', 's',
            't', 'v', 'w', 'x', 'y',
            'z']]


custom = []





def generator():
    for things in range(15):
        text = []
        for let in range(randint(0,10)):            
            text.append(str(words[1][randint(0,4)]))
            text.append(' ')
            for const in range(randint(3,12)):
                text.append(str(words[0][randint(0,20)]))
                text.append(' ')
            text.append('\n')
        field.insert(END, text)
        
           
           

def loading():
    for load in range(20):
        sleep(1)
        bar.step(step_size)
    generator()


button = Button(window, text = 'Generate Text!', command = loading)

bar = Progressbar(window, orient = HORIZONTAL, maximum = 101)

field = Listbox(window, width = 60, height = 20)

margin = 5

field.pack(padx = margin, pady = margin)
button.pack(padx = margin, pady = margin)
bar.pack(pady = margin)

window.mainloop()

