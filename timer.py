from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QHBoxLayout,QLabel,QWidget,QVBoxLayout,QPushButton
from PyQt5.QtCore import Qt
from random import randint

app = QApplication([])
my_win = QWidget()
my_win.setWindowTitle('Мое первое приложение')
my_win.move(900,70)
my_win.resize(400,200)
my_win.show()
v_line = QVBoxLayout()
h_line = QHBoxLayout()

app.exec_()