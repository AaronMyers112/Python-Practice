from turtle import *

class Shape:


    def __init__(self, x, y):
        self.x = x
        self.y = y
    description = 'This Shape has not yet been defined'
    author = 'There is currently no author to this shape'

    def rectangle(self, posx, posy):
        penup()
        goto(posx, posy)
        pendown()
        goto(xcor() + self.x, ycor())
        goto(xcor(), ycor() + self.y)
        goto(xcor() - self.x, ycor())
        goto(xcor(), ycor() - self.y)
        penup()
    
    def triangle(self, posx, posy):
        penup()
        goto(posx, posy)
        pendown()
        goto(xcor() + self.x/2, ycor())
        goto(xcor() - self.x/2, ycor() + self.y)
        goto(xcor() - self.x/2, ycor() - self.y)
        goto(xcor() + self.x/2, ycor())
        penup()
    
    def area (self):
        return self.x * self.y
    
    def perimeter(self):
        return (self.x * 2) + (self.y * 2)

    def description(self, text):
        self.description = text
        
    def authorName(self, text):
        self.authorName = text

    def scaleSize(self, scale):
        self.x = self.x * scale
        self.y = self.y * scale


