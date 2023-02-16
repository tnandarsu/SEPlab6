import turtle

class Disk(object):
    def __init__(self, name="", xpos = 0, ypos = 0, height = 20, width = 40):
        self.dname = name
        self.dxpos = xpos
        self.dypos = ypos
        self.dheight = height
        self.dwidth = width
        self.rect = turtle.Turtle()

    def showdisk(self):
        screen = self.rect.getscreen()
        self.rect.setheading(0)
        self.rect.penup()
        self.rect.goto(self.dxpos, self.dypos)
        self.rect.pendown()

        self.rect.begin_fill()
        for i in range(2):
            self.rect.forward(self.dwidth / 2)
            self.rect.lt(90)
            self.rect.forward(self.dheight)
            self.rect.lt(90)
            self.rect.forward(self.dwidth / 2)
        self.rect.end_fill()

    def newpos(self, xpos, ypos):
        self.dxpos = xpos
        self.dypos = ypos

    def cleardisk(self):
        self.rect.setheading(0)
        self.rect.clear()
        # self.rect.done()

class Pole(object):
    pass

class Hanoi(object):
    pass

