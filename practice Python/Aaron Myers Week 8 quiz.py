from tkinter import *

tkwindow = Tk()

Radio_Variable = BooleanVar()


def options():
    if Radio_Variable.get():
        label1['background'] = 'blue'
        label2['background'] = 'blue'
        label3['background'] = 'blue'
        label4['background'] = 'blue'
        label5['background'] = 'grey'
        label6['background'] = 'blue'
        label7['background'] = 'blue'
        label8['background'] = 'blue'
        label9['background'] = 'blue'

def options2():
    if Radio_Variable.get():
        label1['background'] = 'green'
        label2['bg'] = 'grey'
        label3['bg'] = 'green'
        label4['bg'] = 'grey'
        label5['bg'] = 'grey'
        label6['bg'] = 'grey'
        label7['bg'] = 'green'
        label8['bg'] = 'grey'
        label9['bg'] = 'green'

def options3():
    if Radio_Variable.get():
        label1['bg'] = 'red'
        label2['bg'] = 'grey'
        label3['bg'] = 'red'
        label4['bg'] = 'grey'
        label5['bg'] = 'red'
        label6['bg'] = 'grey'
        label7['bg'] = 'red'
        label8['bg'] = 'grey'
        label9['bg'] = 'red'


label1 = Label(tkwindow, text = "",
               bg = 'grey', width = 5,
               relief = 'groove')
label2 = Label(tkwindow, text = "",
               bg = 'grey', width = 5,
               relief = 'groove')
label3 = Label(tkwindow, text = "",
               bg = 'grey', width = 5,
               relief = 'groove')
label4 = Label(tkwindow, text = "",
               bg = 'grey', width = 5,
               relief = 'groove')
label5 = Label(tkwindow, text = "",
               bg = 'grey', width = 5,
               relief = 'groove')
label6 = Label(tkwindow, text = "",
               bg = 'grey', width = 5,
               relief = 'groove')
label7 = Label(tkwindow, text = "",
               bg = 'grey', width = 5,
               relief = 'groove')
label8 = Label(tkwindow, text = "",
               bg = 'grey', width = 5,
               relief = 'groove')
label9 = Label(tkwindow, text = "",
               bg = 'grey', width = 5,
               relief = 'groove')


choice1 = Radiobutton(tkwindow, text = 'External',
                      variable = Radio_Variable, command = options,
                      value = 1)

choice2 = Radiobutton(tkwindow, text = "Corners",
                      variable = Radio_Variable, command = options2,
                      value = 2)

choice3 = Radiobutton(tkwindow, text = 'Diagonal',
                      variable = Radio_Variable, command =options3,
                      value = 3)


label1.grid(row = 0, column = 0,
            pady = 2)
label2.grid(row = 0, column = 1,
            pady = 2)
label3.grid(row = 0, column = 2,
            pady = 2)
label4.grid(row = 1, column = 0,
            pady = 2)
label5.grid(row = 1, column = 1,
            pady = 2)
label6.grid(row = 1, column = 2,
            pady = 2)
label7.grid(row = 2, column = 0,
            pady = 2)
label8.grid(row = 2, column = 1,
            pady = 2)
label9.grid(row = 2, column = 2,
            pady = 2)


choice1.grid(row = 3, column = 0)
choice2.grid(row = 3, column = 1)
choice3.grid(row = 3, column = 2)

tkwindow.mainloop()
