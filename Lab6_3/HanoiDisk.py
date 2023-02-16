import turtle as t

class Disk(object):
    def __init__(self, name = "", xpos = 0, ypos = 0, height = 20, width = 40) -> None:
        self.dname = name
        self.dxpos = xpos
        self.dypos = ypos
        self.dheight = height
        self.dwidth = width

    def showdisk(self):
        t.goto(self.dxpos, self.dypos)
        self.__turtleDraw()


    def newpos(self, xpos, ypos):
        t.goto(xpos, ypos)
        self.dxpos = xpos
        self.dypos = ypos

    def cleardisk(self):
        t.goto(self.dxpos, self.dypos)
        t.color("white")
        self.__turtleDraw()
        t.color("black")

    def __turtleDraw(self):
        t.pendown()
        t.forward(self.dwidth / 2)
        t.left(90)
        t.forward(self.dheight)
        t.left(90)
        t.forward(self.dwidth)
        t.left(90)
        t.forward(self.dheight)
        t.left(90)
        t.forward(self.dwidth / 2)
        t.penup()