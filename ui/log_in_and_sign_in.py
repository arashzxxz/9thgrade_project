
from ui import styles
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
        self.main_layout.addWidget(self.log_in_button,6,0,6,6)
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
        self.main_layout.addWidget(self.confirm_password_label,5,0,1,1)
        self.main_layout.addWidget(self.confirm_password_entry,5,2,1,4)
        self.main_layout.addWidget(self.show_error_confirm_password,6,0,1,6)
        self.main_layout.addWidget(self.sign_in_button,7,0,6,6)
        self.main_layout.setContentsMargins(150,50,150,0)
        self.setLayout(self.main_layout)
        #------------------



class connect_pages(QWidget):
    def __init__(self):
        super().__init__()
        # create all the widgets
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
        self.choose_tab1.clicked.connect(lambda : self.main_widget.setCurrentIndex(0))
        self.choose_tab2.clicked.connect(lambda : self.main_widget.setCurrentIndex(1))
        self.sign_in_tab.sign_in_button.clicked.connect(self.gather_sign_in_info)
        self.database=database
        #-------------------

    #get entrys text
    def gather_sign_in_info(self,database):
        self.sign_in_tab.show_error_username.setText("")
        self.sign_in_tab.show_error_password.setText("")
        self.sign_in_tab.show_error_confirm_password.setText("")
        user=self.sign_in_tab.username_entry.text()
        password=self.sign_in_tab.password_entry.text()
        confirm_password=self.sign_in_tab.confirm_password_entry.text()
        if not user:
            self.sign_in_tab.show_error_username.setText("Please enter a user name")
        if not password:
            self.sign_in_tab.show_error_password.setText("Please enter a password")
        if not confirm_password:
            self.sign_in_tab.show_error_confirm_password.setText("Please confirm the password")
        if password!=confirm_password:
            self.sign_in_tab.show_error_confirm_password.setText("The passwords dont match each other")
        else :
            exit_code=sign_in.sign_in_backend(user,password,self.database)

    #--------------