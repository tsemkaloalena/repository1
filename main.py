import random

from PyQt5 import uic
from PyQt5.QtCore import Qt, QPoint
import sys

from PyQt5.QtGui import QPaintEvent, QPainter, QColor, QKeyEvent
from PyQt5.QtWidgets import QWidget, QApplication, QLabel


class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        uic.loadUi('UI.ui', self)
        self.WIDTH, self.HEIGHT = 650, 700
        self.flag = False
        self.show()
        self.btn.clicked.connect(self.paint_circle)

    def paint_circle(self):
        self.x = random.randint(0, self.WIDTH)
        self.y = random.randint(0, self.HEIGHT)
        self.d = random.randint(20, 400)
        self.flag = True
        self.repaint()

    def paintEvent(self, QPaintEvent):
        if self.flag:
            painter = QPainter()
            painter.begin(self)
            painter.setBrush(QColor(255, 255, 0))
            painter.drawEllipse(self.x, self.y, self.d, self.d)
            painter.end()
        self.flag = False


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())
