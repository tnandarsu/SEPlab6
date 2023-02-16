import sys
from PySide6.QtWidgets import *
from PySide6.QtCore import *
from PySide6.QtGui import *

class DrawingWindow(QWidget):
    def __init__(self):
        QWidget.__init__(self, None)
        self.setGeometry(0, 0, 500, 100)

        self.drawing = False
        self.brushSize = 12
        self.previousPoint = QPoint()
        self.drawingWindow = QWidget()

        self.image = QImage(self.size(), QImage.Format_RGB32)
        self.image.fill(Qt.white)

    def mousePressEvent(self, event):
        if (event.button() == Qt.LeftButton):
            self.drawing = True
            self.previousPoint = event.pos()

    def mouseMoveEvent(self, e):
        if (e.buttons() and Qt.LeftButton) and self.drawing:
            painter = QPainter(self.image)
            painter.setPen(QPen(Qt.black, self.brushSize))

            painter.drawLine(self.previousPoint, e.pos())

            self.previousPoint = e.pos()
            self.update()




def main():
    app = QApplication(sys.argv)

    return app.exec()

if __name__ == "__main__":
    sys.exit(main())
