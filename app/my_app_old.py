from PyQt5.QtCore import Qt, QTimer, QTime, QLocale
from PyQt5.QtGui import QDoubleValidator, QIntValidator, QFont # проверка типов вводимых значений
from PyQt5.QtWidgets import (
        QApplication, QWidget,
        QHBoxLayout, QVBoxLayout, QGridLayout,
        QGroupBox, QRadioButton,
        QPushButton, QLabel, QListWidget, QLineEdit,QMessageBox)
import instr
import second_win
 
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
        self.hello = QLabel(instr.txt_hello)
        self.hello.setStyleSheet('font-size: 20px')
        # self.text = QLabel(txt_instruction)
        self.btn_inst = QPushButton('Инструкция')
        self.btn_inst.setStyleSheet('font-size:30px')
        self.btn = QPushButton(instr.txt_next)
        self.v_line.addWidget(self.hello,alignment=Qt.AlignCenter)
        self.v_line.addWidget(self.btn_inst,alignment=Qt.AlignCenter)
        self.v_line.addWidget(self.btn,alignment=Qt.AlignCenter)
        self.setLayout(self.v_line)
    # def revise_click(self):
    #     second_win.TestWin.hide()
    #     self.show()

    def next_click(self):
        self.hide()
        self.fw = second_win.TestWin()

    def msg_box(self):
        self.msg = QMessageBox()
        self.msg.setIcon(QMessageBox.information(self,'Инструкция',instr.txt_instruction,QMessageBox.Ok | QMessageBox.Cancel))
        # self.msg.setWindowTitle('Инструкция')
        # self.msg.setText(txt_instruction)
        retval = app.exec()
    
    def connects(self):
        self.btn.clicked.connect(self.next_click)
        self.btn_inst.clicked.connect(self.msg_box)
        # TestWin.btn_down.clicked.connect(self.revise_click())
    
    '''устанавливает, как будет выглядеть окно (надпись, размер, место)'''
    def set_appear(self):
        self.setWindowTitle(instr.txt_title)
        self.resize(instr.win_width,instr.win_height)
        self.move(instr.win_x,instr.win_y)

 
app = QApplication([])
mw = MainWin()

app.exec_()
 
