from ui import Menu,Tabs,styles
from PyQt5.QtSql import QSqlDatabase,QSqlQuery
from PyQt5.QtCore import Qt,QTime,QTimer,QDate,QSize
from PyQt5.QtWidgets import QApplication,QMainWindow,QTreeView,QDateEdit,QTableWidgetItem,QMessageBox,QTabWidget, QWidget,QFileDialog, QLabel,QListWidget ,QComboBox,QPushButton ,QVBoxLayout,QTableWidget,QVBoxLayout,QHBoxLayout,QGridLayout,QCheckBox,QRadioButton,QButtonGroup,QLineEdit
from PyQt5.QtGui import QIcon,QFont,QPixmap,QFontDatabase,QStandardItemModel,QStandardItem


class menu(QWidget):
    def __init__(self):
        super().__init__()

        #create buttons
        self.menu_button=QPushButton("",self)
        self.home_button=QPushButton("",self)
        self.setting_button=QPushButton("",self)
        self.status_button=QPushButton("",self)
        self.menu_button.setIcon(QIcon('C:/Users/r/Contacts/Desktop/9thgrade_project/assets/menu.png'))
        self.home_button.setIcon(QIcon('C:/Users/r/Contacts/Desktop/9thgrade_project/assets/home.png'))
        self.setting_button.setIcon(QIcon('C:/Users/r/Contacts/Desktop/9thgrade_project/assets/setting.png'))
        self.status_button.setIcon(QIcon('C:/Users/r/Contacts/Desktop/9thgrade_project/assets/status.png'))
        size=QSize(40,40)
        self.menu_button.setIconSize(size)
        self.home_button.setIconSize(size)
        self.status_button.setIconSize(size)
        self.setting_button.setIconSize(size)
        self.menu_button.setObjectName("menub")
        self.home_button.setObjectName("homeb")
        self.setting_button.setObjectName("settingb")
        #------------

        #create main layout
        self.menu_layout=QGridLayout(self)
        self.menu_layout.setObjectName("menu_layout")
        self.menu_layout.addWidget(self.menu_button,0,0)
        self.menu_layout.addWidget(self.home_button,1,0)
        self.menu_layout.addWidget(self.status_button,2,0)
        self.menu_layout.addWidget(QLabel(""),3,0)
        self.menu_layout.addWidget(QLabel(""),4,0)
        self.menu_layout.addWidget(self.setting_button,5,0)
        self.setLayout(self.menu_layout)
        #------------------


    #connecting buttons : called in main.py
    def connect_buttons(self,tabs):
        self.home_button.clicked.connect(lambda:tabs.setCurrentIndex(0))
        self.status_button.clicked.connect(lambda:tabs.setCurrentIndex(1))
        self.setting_button.clicked.connect(lambda:tabs.setCurrentIndex(2))
    #-------------------------------------