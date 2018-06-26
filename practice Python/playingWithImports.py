from playingWithClasses import *
from tkinter import *
import turtle

window = Tk()

shapeLabel = Label(window, text = 'What shape would you like to create?')
shape = Entry(window, width = 42)

xLabel = Label(window, text = 'What would you like your x dimension to be?')
sizex = Entry(window)

yLabel = Label(window, text = 'What would you like your \'y\' dimension to be?')
sizey = Entry(window)

posxLabel = Label(window, text = 'What x coordinate would you like your shape to be drawn at?')
posx = Entry(window)

posyLabel = Label(window, text = 'What y coordinate would you like yoru shape to be drawn at?')
posy = Entry(window)






button = Button(window, text = 'Draw!',
                command = lambda: draw())



def draw():
    shapeInfo = shape.get()
    xInfo = sizex.get()
    yInfo = sizey.get()
    posxInfo = posx.get()
    posyInfo = posy.get()
    print(shapeInfo)
    print(xInfo)
    print(yInfo)
    print(posxInfo)
    print(posyInfo)
    if shapeInfo == 'triangle':
        canvas = Canvas(window, width = 100,
                        height = 100)
        print('triangle')
        t = turtle.RawTurtle(canvas)
        t.triangle = Shape(int(xInfo), int(yInfo))
        t.triangle.triangle(int(posxInfo), int(posyInfo))
        triangle.triangle(int(posxInfo), int(posyInfo))

##    elif shape.get() == 'RECTANGLE':
##        sizex, sizey = input('What size would you like your Rectangle? ').split()
##        shape = Shape(int(sizex), int(sizey))
##        posx, posy = input('Where would you like your rectangle to be drawn? ').split()
##        shape.rectangle(int(posx), int(posy))

    canvas.grid(row = 4, column = 0, columnspan = 5)
button.grid(row =3, column = 2)
shapeLabel.grid(row = 0, column = 1,
                columnspan = 2, padx = 5,
                pady = 5)
shape.grid(row = 0, column = 2,
           columnspan = 2, padx = 5,
                pady = 5)
xLabel.grid(row = 1, column = 0,
            padx = 5, pady = 5)
sizex.grid(row = 1, column = 1,
            padx = 5, pady = 5)
yLabel.grid(row = 2, column = 0,
            padx = 5, pady = 5)
sizey.grid(row = 2, column = 1,
            padx = 5, pady = 5)
posxLabel.grid(row = 1, column = 3,
            padx = 5, pady = 5)
posx.grid(row = 1, column = 4,
            padx = 5, pady = 5)
posyLabel.grid(row = 2, column = 3,
            padx = 5, pady = 5)
posy.grid(row = 2, column = 4,
            padx = 5, pady = 5)


window.mainloop()
