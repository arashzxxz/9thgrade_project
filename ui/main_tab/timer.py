#import
import sys
from PyQt5.QtCore import Qt,QTime,QTimer
from PyQt5.QtWidgets import QApplication,QMainWindow, QWidget, QLabel ,QPushButton ,QVBoxLayout,QVBoxLayout,QHBoxLayout,QGridLayout,QCheckBox,QRadioButton,QButtonGroup,QLineEdit
from PyQt5.QtGui import QIcon,QFont,QPixmap,QFontDatabase
#main app obj
class Timer(QWidget):
    def __init__(self):
        super().__init__()
        # create the widgets
        self.setWindowTitle("stop watch")
        self.setGeometry(760,390,400,300)
        self.setWindowIcon(QIcon("c"))
        self.time=QTime(00,00,00,00)
        self.t_label=QLabel(self.Formatt(self.time),self)
        self.startb=QPushButton("Start",self)
        self.stopb=QPushButton("Stop",self)
        self.resetb=QPushButton("Reset",self)
        self.timer=QTimer(self)
        #-------------------

        # set the layout
        self.main_layout=QHBoxLayout(self)
        self.main_layout.addWidget(self.t_label)
        self.setLayout(self.main_layout)
        self.t_label.setAlignment(Qt.AlignCenter)
        self.hbox=QVBoxLayout(self)
        self.hbox.addWidget(self.startb)
        self.hbox.addWidget(self.stopb)
        self.hbox.addWidget(self.resetb)
        self.main_layout.addLayout(self.hbox)
        #---------------

    def connect_buttons(self):
        self.startb.clicked.connect(self.Start)
        self.stopb.clicked.connect(self.Stop)
        self.resetb.clicked.connect(self.Reset)
        self.timer.timeout.connect(self.update)
    def Start(self):
        self.timer.start(10)
    def Stop(self):
        self.timer.stop()
    def Reset(self):
        self.timer.stop()
        self.time=QTime(00,00,00,00)
        self.t_label.setText(self.Formatt(self.time))
    def Formatt(self,time):
        h=self.time.hour()
        m=self.time.minute()
        s=self.time.second()
        mm=self.time.msec() //10
        return f"{h:02}:{m:02}:{s:02}.{mm:02}"

    def update(self):
        self.time=self.time.addMSecs(10)
        self.t_label.setText(self.Formatt(self.time))

