from PyQt5.QtWidgets import (QApplication, QMainWindow, QTreeView, QDateEdit, QTableWidgetItem,   
                             QMessageBox, QTabWidget, QWidget, QFileDialog, QLabel, QListWidget,   
                             QComboBox, QPushButton, QVBoxLayout, QTableWidget, QHBoxLayout,   
                             QGridLayout, QCheckBox, QRadioButton, QButtonGroup, QLineEdit)  
from PyQt5.QtCore import Qt  
from users import current_user  


class Menu(QWidget):  
    def __init__(self):  
        super().__init__()  
        self.home_times=0
        # Create buttons and group them  
        self.menu_button = QRadioButton("Menu", self)  
        self.home_button = QRadioButton("Home", self)  
        self.setting_button = QRadioButton("Settings", self)  
        self.status_button = QRadioButton("Status", self)  
        self.users_button = QRadioButton("Users", self)
        self.menu_button.setObjectName("menub")  
        self.home_button.setObjectName("homeb")  
        self.status_button.setObjectName("statusb")  
        self.setting_button.setObjectName("settingb")  
        self.users_button.setObjectName("usersb")  
        self.menus_buttons_group = QButtonGroup(self)  
        self.menus_buttons_group.addButton(self.menu_button)  
        self.menus_buttons_group.addButton(self.home_button)  
        self.menus_buttons_group.addButton(self.status_button)  
        self.menus_buttons_group.addButton(self.setting_button)  
        self.menus_buttons_group.addButton(self.users_button)  
        self.setContentsMargins(10, 10, 0, 10)  
        #--------------------------

        # Create main layout  
        self.menu_layout = QGridLayout(self)  
        self.menu_layout.setObjectName("menu_layout")  
        self.menu_layout.addWidget(self.menu_button, 0, 0)  
        self.menu_layout.addWidget(self.home_button, 1, 0)  
        self.menu_layout.addWidget(self.status_button, 2, 0)  
        self.menu_layout.addWidget(QLabel(""), 3, 0)  # Spacer  
        self.menu_layout.addWidget(QLabel(""), 4, 0)  # Spacer  
        self.menu_layout.addWidget(self.users_button, 5, 0)  
        self.menu_layout.addWidget(self.setting_button, 6, 0)  
        self.menu_layout.setContentsMargins(0, 0, 0, 0)  
        self.setLayout(self.menu_layout)  
        #-------------------
    # Connecting buttons: called in main.py  
    def connect_buttons(self, tabs,tab,tab2):  
        self.home_button.clicked.connect(lambda: self.home_button_clicked_function(tabs,tab))   
        self.setting_button.clicked.connect(lambda: tabs.setCurrentIndex(2))  
        self.users_button.clicked.connect(lambda: tabs.setCurrentIndex(4))  
        self.menu_button.clicked.connect(self.expand_menu)  
        self.status_button.clicked.connect(lambda : self.expand_chart_tab(tabs,tab2))  
    #--------------------------------------    

    def expand_chart_tab(self,tabs,tab2):
        if current_user.logged_in_user.log_in_status == True :
            tab2.create_the_chart()
            tabs.setCurrentIndex(9) 
        if current_user.logged_in_user.log_in_status == False:   
            tabs.setCurrentIndex(6)  
    # Home button clicked  
    def home_button_clicked_function(self, tabs,tab):  
        if current_user.logged_in_user.log_in_status == True:  
            tabs.setCurrentIndex(7)
            if self.home_times==0:
                tab.get_schedules()
                self.home_times=1
        if current_user.logged_in_user.log_in_status == False:   
            tabs.setCurrentIndex(6)  
    #--------------------

    # Expand menu function  
    def expand_menu(self):  
        # Toggle visibility of texts
        if not self.home_button.text():
            self.menu_button.setText("Menu") 
            self.home_button.setText("Home") 
            self.setting_button.setText("Settings") 
            self.status_button.setText("Status")  
            self.users_button.setText("User")
        else:
            self.menu_button.setText("") 
            self.home_button.setText("") 
            self.setting_button.setText("") 
            self.status_button.setText("")  
            self.users_button.setText("")
        #-----------------------------
    #-----------------------