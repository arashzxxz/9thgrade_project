
from ui import styles
import re
from users import sign_in,log_in
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QScrollArea,QStackedWidget,QDateEdit,QTableWidgetItem,QMessageBox,QTabWidget, QWidget,QFileDialog, QLabel,QListWidget ,QComboBox,QPushButton ,QVBoxLayout,QTableWidget,QVBoxLayout,QHBoxLayout,QGridLayout,QCheckBox,QRadioButton,QButtonGroup,QLineEdit
from PyQt5.QtGui import QIcon,QFont


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
        self.show_error_username=QLabel("",self)
        self.show_error_username.setStyleSheet("background-color: transparent;")
        self.show_error_username.setAlignment(Qt.AlignCenter)
        self.show_error_password=QLabel("",self)
        self.show_error_password.setStyleSheet("background-color: transparent;")
        self.show_error_password.setAlignment(Qt.AlignCenter)
        self.show_error_overall=QLabel("",self)
        self.show_error_overall.setStyleSheet("background-color: transparent;")
        self.show_error_overall.setAlignment(Qt.AlignCenter)
        #----------------------

        #create the layout
        self.main_layout=QGridLayout(self)
        self.main_layout.addWidget(self.header,0,0,1,6)
        self.main_layout.addWidget(self.username_label,1,0,1,1)
        self.main_layout.addWidget(self.username_entry,1,2,1,4)
        self.main_layout.addWidget(self.show_error_username,2,0,1,6)
        self.main_layout.addWidget(self.password_label,3,0,1,1)
        self.main_layout.addWidget(self.password_entry,3,2,1,4)
        self.main_layout.addWidget(self.show_error_password,4,0,1,6)
        self.main_layout.addWidget(self.show_error_overall,6,0,1,6)
        self.main_layout.addWidget(self.log_in_button,7,0,6,6)
        self.main_layout.setContentsMargins(150,50,150,0)
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
        self.sign_in_button=QPushButton("Sign in",self)
        self.username_label=QLabel("User name : ",self)
        self.confirm_password_label=QLabel("Confirm password  : ",self)
        self.confirm_password_entry=QLineEdit(self)
        self.show_error_username=QLabel("",self)
        self.show_error_username.setStyleSheet("background-color: transparent;")
        self.show_error_username.setAlignment(Qt.AlignCenter)
        self.show_error_password=QLabel("",self)
        self.show_error_password.setStyleSheet("background-color: transparent;")
        self.show_error_password.setAlignment(Qt.AlignCenter)
        self.show_status_password=QLabel("Password Security : Very weak",self)
        self.show_status_password.setStyleSheet("background-color: transparent;")
        self.show_status_password.setAlignment(Qt.AlignCenter)
        self.show_error_overall=QLabel("",self)
        self.show_error_overall.setStyleSheet("background-color: transparent;")
        self.show_error_overall.setAlignment(Qt.AlignCenter)
        self.show_error_confirm_password=QLabel("",self)
        self.show_error_confirm_password.setStyleSheet("background-color: transparent;")
        self.show_error_confirm_password.setAlignment(Qt.AlignCenter)
        #----------------------

        #create the layout
        self.main_layout=QGridLayout(self)
        self.main_layout.addWidget(self.header,0,0,1,6)
        self.main_layout.addWidget(self.username_label,1,0,1,1)
        self.main_layout.addWidget(self.username_entry,1,2,1,4)
        self.main_layout.addWidget(self.show_error_username,2,0,1,6)
        self.main_layout.addWidget(self.password_label,3,0,1,1)
        self.main_layout.addWidget(self.password_entry,3,2,1,4)
        self.main_layout.addWidget(self.show_error_password,4,0,1,6)
        self.main_layout.addWidget(self.show_status_password,5,0,1,6)
        self.main_layout.addWidget(self.confirm_password_label,6,0,1,1)
        self.main_layout.addWidget(self.confirm_password_entry,6,2,1,4)
        self.main_layout.addWidget(self.show_error_confirm_password,7,0,1,6)
        self.main_layout.addWidget(self.show_error_overall,8,0,1,6)
        self.main_layout.addWidget(self.sign_in_button,9,0,6,6)
        self.main_layout.setContentsMargins(150,50,150,0)
        self.setLayout(self.main_layout)
        #------------------



class connect_pages(QWidget):
    def __init__(self):
        super().__init__()
        # create all the widgets
        self.password_security=0
        self.justwhitespace_pattern=re.compile(r"(^\s*$)")
        self.existwhitespace_pattern=re.compile(r"\s+")
        self.security_pattern=[re.compile(r"\d+"),re.compile(r"\W+"),re.compile(r".{8}")]
        self.main_widget=QStackedWidget(self)
        self.log_in_tab=Log_in()
        self.sign_in_tab=Sign_in()
        self.choose_tab1=QPushButton("Log ing",self)
        self.choose_tab2=QPushButton("Sign in",self)
        #-----------------------

        # create layouts
        self.main_widget.addWidget(self.log_in_tab)
        self.main_widget.addWidget(self.sign_in_tab)
        self.main_layout=QVBoxLayout(self)
        self.choose_tab_layout=QVBoxLayout(self)
        self.choose_tab_layout.addWidget(self.choose_tab1)
        self.choose_tab_layout.addWidget(self.choose_tab2)
        self.choose_tab_layout.setContentsMargins(350,0,350,0)
        self.main_layout.addWidget(self.main_widget)
        self.main_layout.addLayout(self.choose_tab_layout)
        self.setLayout(self.main_layout)
        #---------------

    #connect all buttons
    def connect_buttons(self,tabs,database):
        self.sign_in_tab.password_entry.textChanged.connect(self.change_password_entry_error_and_security)
        self.sign_in_tab.confirm_password_entry.textChanged.connect(lambda : self.sign_in_tab.show_error_confirm_password.setText(""))
        self.sign_in_tab.username_entry.textChanged.connect(lambda : self.sign_in_tab.show_error_username.setText(""))
        self.sign_in_tab.confirm_password_entry.textChanged.connect(lambda : self.sign_in_tab.show_error_overall.setText(""))
        self.sign_in_tab.username_entry.textChanged.connect(lambda : self.sign_in_tab.show_error_overall.setText(""))
        self.choose_tab1.clicked.connect(lambda : self.main_widget.setCurrentIndex(0))
        self.choose_tab2.clicked.connect(lambda : self.main_widget.setCurrentIndex(1))
        self.database=database
        self.sign_in_tab.sign_in_button.clicked.connect(self.gather_sign_in_info)
        self.log_in_tab.log_in_button.clicked.connect(self.gather_log_in_info)
    #-------------------


    # show the password security status
    def change_password_entry_error_and_security(self):
        self.password_security=0
        self.sign_in_tab.show_error_password.setText("")
        if self.security_pattern[0].findall(self.sign_in_tab.password_entry.text()):
            self.password_security=self.password_security+1
        if self.security_pattern[1].findall(self.sign_in_tab.password_entry.text()):
            self.password_security=self.password_security+1
        if self.security_pattern[2].findall(self.sign_in_tab.password_entry.text()):
            self.password_security=self.password_security+1
        if self.password_security==1:
            self.sign_in_tab.show_status_password.setText("Password Security : Weak")
        if self.password_security==2:
            self.sign_in_tab.show_status_password.setText("Password Security : Medium")
        if self.password_security==3:
            self.sign_in_tab.show_status_password.setText("Password Security : Strong")

    #------------------------------------


    #get sign in entrys text and handle errors
    def gather_sign_in_info(self):
        
        self.sign_in_tab.show_error_overall.setText("")
        self.sign_in_tab.show_error_username.setText("")
        self.sign_in_tab.show_error_password.setText("")
        self.sign_in_tab.show_error_confirm_password.setText("")
        user=self.sign_in_tab.username_entry.text()
        password=self.sign_in_tab.password_entry.text()
        confirm_password=self.sign_in_tab.confirm_password_entry.text()
        if not user :
            self.sign_in_tab.show_error_username.setText("Please enter a user name")
        if self.justwhitespace_pattern.findall(user) :
            self.sign_in_tab.show_error_username.setText("Please enter a user name")
        if not password:
            self.sign_in_tab.show_error_password.setText("Please enter a password")
        if self.existwhitespace_pattern.findall(password) :
            self.sign_in_tab.show_error_password.setText("White Spaces are not allowed in the password")
        if self.justwhitespace_pattern.findall(password) :
            self.sign_in_tab.show_error_password.setText("Please enter a password")
        if not confirm_password:
            self.sign_in_tab.show_error_confirm_password.setText("Please confirm the password")
        if self.justwhitespace_pattern.findall(confirm_password) :
            self.sign_in_tab.show_error_confirm_password.setText("Please confirm the password")
        if password!=confirm_password:
            self.sign_in_tab.show_error_confirm_password.setText("The passwords dont match each other")
        else :
            exit_code=sign_in.sign_in_backend(user,password,self.database)
            if exit_code=="409":
                self.sign_in_tab.show_error_overall.setText(f"user already exists , error code : {exit_code}")
            if exit_code=="0":
                self.log_in_tab.show_error_overall.setText(f"Account successfully created")

    #--------------------------------

    #get log in entrys text and handle errors
    def gather_log_in_info(self):
        self.log_in_tab.show_error_overall.setText("")
        self.log_in_tab.show_error_username.setText("")
        self.log_in_tab.show_error_password.setText("")
        user=self.log_in_tab.username_entry.text()
        password=self.log_in_tab.password_entry.text()
        if not user :
            self.log_in_tab.show_error_username.setText("Please enter a user name")
        if self.justwhitespace_pattern.findall(user) :
            self.log_in_tab.show_error_username.setText("Please enter a user name")
        if not password:
            self.log_in_tab.show_error_password.setText("Please enter a password")
        if self.existwhitespace_pattern.findall(password) :
            self.log_in_tab.show_error_password.setText("White Spaces are not allowed in the password")
        if self.justwhitespace_pattern.findall(password) :
            self.log_in_tab.show_error_password.setText("Please enter a password")
        else :
            exit_code=log_in.log_in_backend(user,password,self.database)
            if exit_code=="404":
                self.log_in_tab.show_error_overall.setText(f"user does not exist , error code : {exit_code}")
            if exit_code=="255,u and p dont match":
                self.log_in_tab.show_error_overall.setText(f"Username and password dont match each other")
            if exit_code=="0":
                self.log_in_tab.show_error_overall.setText(f"Successfully logged in")

    #--------------------------------