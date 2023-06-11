from PyQt5.QtCore import Qt
from PyQt5.QtGui import QFont
from PyQt5.QtWidgets import QApplication, QHBoxLayout,QLabel,QWidget,QVBoxLayout,QPushButton
from random import randint

def show_winner():
    num = str(randint(1,100))
    winner.setText(num)
    text.setText('Победитель:')
app = QApplication([])
my_win = QWidget()
my_win.setWindowTitle('Мое первое приложение')
my_win.move(900,70)
my_win.resize(400,200)
my_win.show()
v_line = QVBoxLayout()
h_line = QHBoxLayout()
text = QLabel('?')
winner = QLabel('Победитель:')
winner.text()
button = QPushButton('Подтвердить')
v_line.addWidget(
    text,alignment=Qt.AlignCenter
)
v_line.addWidget(
    winner,alignment= Qt.AlignCenter
)
v_line.addWidget(
    button,alignment=Qt.AlignCenter
)
button.clicked.connect(show_winner)
my_win.setLayout(v_line)
my_win.setLayout(h_line)
app.exec_()
