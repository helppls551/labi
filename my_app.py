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
        pass
    
    def next_click(self):
        pass
    
    def connects(self):
        pass
    
    ''' устанавливает, как будет выглядеть окно (надпись, размер, место) '''
    def set_appear(self):
        pass
 
app = QApplication([])
mw = MainWin()
app.exec_()
 
