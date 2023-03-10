import sys
from PySide6.QtCore import *
from PySide6.QtWidgets import *
from PySide6.QtGui import *
from PySide6.QtGui import QPainter, QBrush, QPen


class Simple_drawing_window(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)
        self.setWindowTitle("Simple Drawing")
        self.rabbit = QPixmap("images/rabbit.png")

    def paintEvent(self, e):
        p = QPainter()
        p.begin(self)

        p.setPen(QColor(0, 0, 0))
        p.setBrush(QColor(0, 127, 0))
        p.drawPolygon(
            [QPoint(70, 100), QPoint(100, 110),
            QPoint(130, 100), QPoint(100, 150),]
        )

        p.setPen(QColor(255, 127, 0))
        p.setBrush(QColor(255, 127, 0))
        p.drawPie(50, 150, 100, 100, 0, 180 * 16)

        p.drawPolygon(
            [QPoint(50, 200), QPoint(150, 200), QPoint(100, 400),]
        )

        p.drawPixmap(QRect(200, 100, 320, 320), self.rabbit)
        p.end()

class Simple_drawing_window1(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)
        self.setWindowTitle("Simple Drawing")
        self.apple = QPixmap("images/apple.png")

    def paintEvent(self, e):
        p = QPainter()
        p.begin(self)

        p.drawPixmap(QRect(200, 100, 320, 320), self.apple)
        p.end()
        
class Simple_drawing_window2(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)
        self.setWindowTitle("Simple Drawing2")
        self.rabbit = QPixmap("images/rabbit.png")
    
    def paintEvent(self, e):
        paint = QPainter()
        paint.begin(self)

        # make a white drawing background
        paint.setBrush(Qt.white)

        # for circle make the ellipse radii match
        radx = 100
        rady = 100
        # draw red circles
        paint.setPen(Qt.red)
        for k in range(125, 220, 10):
            center = QPoint(k, k)
            # optionally fill each circle yellow
            paint.setBrush(Qt.yellow)
            paint.drawEllipse(center, radx, rady)
        paint.drawPixmap(QRect(200, 100, 320, 320), self.rabbit)
        paint.end()
        

class Simple_drawing_window_3(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)
        self.setWindowTitle("Simple Drawing Window 3")
        self.rabbit = QPixmap("images/rabbit.png")

    def paintEvent(self, e):
        p = QPainter()
        p.begin(self)

        p.setPen(QColor(0, 0, 0))
        p.setBrush(QColor(0, 127, 0))
        for x in range(24):
            p.drawEllipse(250, 250, 100, 100)
            p.rotate(15)
        p.end()

def main():
    app = QApplication(sys.argv)

    w = Simple_drawing_window()
    w.show()
    
    w2 = Simple_drawing_window2()
    w2.show()
    
    w3 = Simple_drawing_window_3()
    w3.show()

    w1 = Simple_drawing_window1()
    w1.show()

    return app.exec()

if __name__ == "__main__":
    sys.exit(main())
