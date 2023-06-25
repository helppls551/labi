from PyQt5.QtCore import Qt, QTimer, QTime, QLocale
from PyQt5.QtGui import QDoubleValidator, QIntValidator, QFont # проверка типов вводимых значений
from PyQt5.QtWidgets import (
        QApplication, QWidget,
        QHBoxLayout, QVBoxLayout, QGridLayout,
        QGroupBox, QRadioButton,
        QPushButton, QLabel, QListWidget, QLineEdit)
 
from instr import *
from second_win import *
 
class MainWin(QWidget):
    def __init__(self):
        ''' окно, в котором располагается приветствие '''
        super().__init__()
    
        #устанавливает, как будет выглядеть окно (надпись, размер, место)
        self.set_appear()
    
        # создаём и настраиваем графические элементы:
        self.initUI()
    
        #устанавливает связи между элементами
        self.connects()
    
        # старт:
        self.show()
    
    def initUI(self):
        ''' создаёт графические элементы '''
        self.v_line = QVBoxLayout()
        self.hello = QLabel(txt_hello)
        self.text = QLabel(txt_instruction)
        self.btn = QPushButton(txt_next)
        self.v_line.addWidget(self.hello,alignment=Qt.AlignLeft)
        self.v_line.addWidget(self.text,alignment=Qt.AlignLeft)
        self.v_line.addWidget(self.btn,alignment=Qt.AlignCenter)
        self.setLayout(self.v_line)
    
    def next_click(self):
        self.hide()
        self.fw = TestWin()
 
    
    def connects(self):
        self.btn.clicked.connect(self.next_click)
    
    '''устанавливает, как будет выглядеть окно (надпись, размер, место)'''
    def set_appear(self):
        self.setWindowTitle(txt_title)
        self.resize(win_width,win_height)
        self.move(win_x,win_y)

 
app = QApplication([])
mw = MainWin()

app.exec_()
 
