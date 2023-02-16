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
        self.rect.done()

class Pole(object):
    def __init__(self, name="", xpos=0, ypos=0, thick=10, length=100):
        self.pname = name
        self.stack = []
        self.toppos = 0
        self.pxpos = xpos
        self.pypos = ypos
        self.pthick = thick
        self.plength = length

    def showpole(self):
        turtle.penup()
        turtle.goto(self.pxpos, self.pypos)
        turtle.pendown()

        turtle.forward(self.pthick/2)
        turtle.left(90)
        turtle.forward(self.plength)
        turtle.left(90)
        turtle.forward(self.pthick)
        turtle.left(90)
        turtle.forward(self.plength)
        turtle.left(90)
        turtle.forward(self.pthick/2)

    def pushdisk(self, disk):
        disk.newpos(self.pxpos, self.toppos)
        disk.showdisk()

        self.toppos += disk.dheight
        self.stack.append(disk)

    def popdisk(self):
        outputdisk = self.stack.pop()
        self.toppos -= outputdisk.dheight

        outputdisk.newpos(self.pxpos, self.toppos)
        outputdisk.cleardisk()

myPole = Pole()
myPole.showpole()

class Hanoi(object):
    def __init__(self, n=3, start="A", workspace="B", destination="C"):
        self.startup = Pole(start,0,0)
        self.workspacep = Pole(workspace,150,0)
        self.destinationp = Pole(destination, 300, 0)
        self.startp.showpole()
        self.workspacep.showpole()
        self.destinationp.showpole()
        for i in range(n):
            self.startp.pushdis(Disk("d" + str(i), 0, i*150,20,(n-i)*30))

    def move_disk(self, start, destination):
        disk = start.popdisk()
        destination.pushdisk(disk)

    def move_tower(self,n,s,d,w):
        if n == 1:
            self.move_disk(s,d)
        else:
            self.move_tower(n-1,s,w,d)
            self.move_disk(s,d)
            self.move_tower(n-1,w,d,s)

    def solve(self):
        self.move_tower(3, self.startp, self.destination, self.workspacep)

h = Hanoi()
h.solve()

