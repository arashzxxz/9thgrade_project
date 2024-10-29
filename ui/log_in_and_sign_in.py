
from ui import styles
from PyQt5.QtSql import QSqlDatabase,QSqlQuery
from PyQt5.QtCore import Qt,QTime,QTimer,QDate,QSize
from PyQt5.QtWidgets import QApplication,QMainWindow,QTreeView,QTimeEdit,QScrollArea,QStackedWidget,QDateEdit,QTableWidgetItem,QMessageBox,QTabWidget, QWidget,QFileDialog, QLabel,QListWidget ,QComboBox,QPushButton ,QVBoxLayout,QTableWidget,QVBoxLayout,QHBoxLayout,QGridLayout,QCheckBox,QRadioButton,QButtonGroup,QLineEdit
from PyQt5.QtGui import QIcon,QFont,QPixmap,QFontDatabase


class Log_in(QWidget):
    def __init__(self):
        super().__init__()
        #create all the widgets
        self.header=QLabel("Log in",self)
        self.header.setAlignment(Qt.AlignCenter)
        self.password_label=QLabel("Password  : ",self)
        self.username_entry=QLineEdit(self)
        self.password_entry=QLineEdit(self)
        self.log_in_button=QPushButton("Log in",self)
        self.username_label=QLabel("User name : ",self)
        #----------------------

        #create the layout
        self.main_layout=QGridLayout(self)
        self.main_layout.addWidget(self.header,0,0,1,6)
        self.main_layout.addWidget(self.username_label,1,0,1,1)
        self.main_layout.addWidget(self.username_entry,1,2,1,4)
        self.main_layout.addWidget(QLabel("",self),2,0,1,1)
        self.main_layout.addWidget(self.password_label,3,0,1,1)
        self.main_layout.addWidget(self.password_entry,3,2,1,4)
        self.main_layout.addWidget(self.log_in_button,4,0,6,6)
        self.main_layout.setContentsMargins(150,50,150,100)
        self.setLayout(self.main_layout)
        #------------------


class Sign_in(QWidget):
    def __init__(self):
        super().__init__()
        #create all the widgets
        self.header=QLabel("Sign in",self)
        self.header.setAlignment(Qt.AlignCenter)
        self.password_label=QLabel("Password  : ",self)
        self.username_entry=QLineEdit(self)
        self.password_entry=QLineEdit(self)
        self.log_in_button=QPushButton("Sign in",self)
        self.username_label=QLabel("User name : ",self)
        self.confirm_password_label=QLabel("Confirm password  : ",self)
        self.confirm_password_entry=QLineEdit(self)
        #----------------------

        #create the layout
        self.main_layout=QGridLayout(self)
        self.main_layout.addWidget(self.header,0,0,1,6)
        self.main_layout.addWidget(self.username_label,1,0,1,1)
        self.main_layout.addWidget(self.username_entry,1,2,1,4)
        self.main_layout.addWidget(QLabel("",self),2,0,1,1)
        self.main_layout.addWidget(self.password_label,3,0,1,1)
        self.main_layout.addWidget(self.password_entry,3,2,1,4)
        self.main_layout.addWidget(QLabel("",self),4,0,1,1)
        self.main_layout.addWidget(self.confirm_password_label,5,0,1,1)
        self.main_layout.addWidget(self.confirm_password_entry,5,2,1,4)
        self.main_layout.addWidget(self.log_in_button,6,0,6,6)
        self.main_layout.setContentsMargins(150,50,150,100)
        self.setLayout(self.main_layout)
        #------------------