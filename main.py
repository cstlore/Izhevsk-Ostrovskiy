from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow, QLabel, QGridLayout
from PyQt5.QtGui import QPainter, QPixmap, QPen, QColor
from PyQt5.QtCore import Qt
from PyQt5 import uic
from random import randint


class Ui(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi('Ui.ui', self)

        self.draw_button.setFixedSize(100, 100)
        self.draw_button.clicked.connect(self.paint)

        self.label = QLabel()
        canvas = QPixmap(600, 600)
        self.label.setPixmap(canvas)

        layout = QGridLayout(self.centralwidget)
        layout.addWidget(self.label, 1, 0)
        layout.addWidget(self.draw_button, 0, 0, alignment=Qt.AlignCenter)

    def paint(self):
        x, y = [randint(10, 500) for i in range(2)]
        w = randint(10, 100)
        h = w
        painter = QPainter(self.label.pixmap())
        pen = QPen()
        pen.setWidth(3)
        pen.setColor(QColor('#FFFF00'))
        painter.setPen(pen)
        painter.drawEllipse(x, y, w, h)
        painter.end()
        self.update()


if __name__ == '__main__':
    import sys

    app = QApplication(sys.argv)
    w = Ui()
    w.show()
    sys.exit(app.exec_())
