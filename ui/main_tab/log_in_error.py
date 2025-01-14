from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout,QStackedWidget,  QLabel, QListWidget, QMessageBox,QPushButton
from ui.main_tab import timer,exercise_suggestion

class Log_in_error_tab(QWidget):  
    def __init__(self):  
        super().__init__()  

        #create the widgets 
        self.error_text=QLabel("Please log in",self)
        self.error_text.setAlignment(Qt.AlignCenter)
        self.vb=QVBoxLayout()
        self.vb.addWidget(self.error_text)
        self.setLayout(self.vb)
        #------------------