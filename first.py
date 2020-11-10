import sys

from PyQt5 import uic  # Импортируем uic
from PyQt5.QtWidgets import QApplication, QMainWindow
from PyQt5.QtGui import QPainter, QColor
from random import randint


class MyWidget(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('1.ui', self)  # Загружаем дизайн
        self.pushButton.clicked.connect(self.run)
        self.test = None
        # Обратите внимание: имя элемента такое же как в QTDesigner

    def run(self):
        self.test = True
        self.update()
        # Имя элемента совпадает с objectNae в QTDesigner

    def paintEvent(self, event):
        if self.test:
            qp = QPainter()
            qp.begin(self)
            self.draw_circle(qp)
            qp.end

    def draw_circle(self, qp):
        qp.setBrush(QColor(255, 255, 0))
        self.radius = randint(0, self.height())
        self.x, self.y = randint(0, self.width()), randint(0, self.height())
        qp.drawEllipse(self.x - self.radius, self.y - self.radius, 2 * self.radius, 2 * self.radius)
        self.test = None

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MyWidget()
    ex.show()
    sys.exit(app.exec_())
