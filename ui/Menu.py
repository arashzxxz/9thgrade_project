from ui import Menu, Settings_Tab,styles
from PyQt5.QtWidgets import QApplication,QMainWindow,QTreeView,QDateEdit,QTableWidgetItem,QMessageBox,QTabWidget, QWidget,QFileDialog, QLabel,QListWidget ,QComboBox,QPushButton ,QVBoxLayout,QTableWidget,QVBoxLayout,QHBoxLayout,QGridLayout,QCheckBox,QRadioButton,QButtonGroup,QLineEdit
from PyQt5.QtGui import QIcon,QFont,QPixmap,QFontDatabase,QStandardItemModel,QStandardItem
from PyQt5.QtCore import QSize


class menu(QWidget):
    def __init__(self):
        super().__init__()
        #create buttons and groupe them
        self.menu_button=QRadioButton("",self)
        self.home_button=QRadioButton("",self)
        self.setting_button=QRadioButton("",self)
        self.status_button=QRadioButton("",self)
        self.menu_button.setObjectName("menub")
        self.home_button.setObjectName("homeb")
        self.status_button.setObjectName("statusb")
        self.setting_button.setObjectName("settingb")
        self.menus_buttons_group=QButtonGroup(self)
        self.menus_buttons_group.addButton(self.menu_button)
        self.menus_buttons_group.addButton(self.home_button)
        self.menus_buttons_group.addButton(self.status_button)
        self.menus_buttons_group.addButton(self.setting_button)
        self.setContentsMargins(10,10,0,10)


        #-------------------------------

        #create main layout
        self.menu_layout=QGridLayout(self)
        self.menu_layout.setObjectName("menu_layout")
        self.menu_layout.addWidget(self.menu_button,0,0)
        self.menu_layout.addWidget(self.home_button,1,0)
        self.menu_layout.addWidget(self.status_button,2,0)
        self.menu_layout.addWidget(QLabel(""),3,0)
        self.menu_layout.addWidget(QLabel(""),4,0)
        self.menu_layout.addWidget(self.setting_button,5,0)
        self.menu_layout.setContentsMargins(0,0,0,0)
        self.setLayout(self.menu_layout)
        #------------------


    #connecting buttons : called in main.py
    def connect_buttons(self,tabs):
        self.home_button.clicked.connect(lambda:tabs.setCurrentIndex(0))
        self.status_button.clicked.connect(lambda:tabs.setCurrentIndex(1))
        self.setting_button.clicked.connect(lambda:tabs.setCurrentIndex(2))
        self.menu_button.clicked.connect(self.expand_menu)
    #-------------------------------------
    def expand_menu(self):
        pass