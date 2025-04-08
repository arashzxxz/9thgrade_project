
from ui import styles
from PyQt5.QtSql import QSqlDatabase,QSqlQuery
from PyQt5.QtCore import Qt,QTime,QTimer,QDate,QSize
from PyQt5.QtWidgets import QApplication,QMainWindow,QTreeView,QTimeEdit,QScrollArea,QStackedWidget,QDateEdit,QTableWidgetItem,QMessageBox,QTabWidget, QWidget,QFileDialog, QLabel,QListWidget ,QComboBox,QPushButton ,QVBoxLayout,QTableWidget,QVBoxLayout,QHBoxLayout,QGridLayout,QCheckBox,QRadioButton,QButtonGroup,QLineEdit
from PyQt5.QtGui import QIcon,QFont,QPixmap,QFontDatabase
from calculations import check_time

class setting_tab(QWidget):
    def __init__(self,database):
        super().__init__()
        #create all the widgets
        self.database=database
        self.customization_header=QLabel("Customization",self)
        self.section_seperator1=QLabel("",self)
        self.notification_header=QLabel("Notification",self)
        self.section_seperator2=QLabel("",self)
        self.data_header=QLabel("Data",self)
        self.section_seperator3=QLabel("",self)
        self.data_header.setObjectName("header3")
        self.notification_header.setObjectName("header2")
        self.customization_header.setObjectName("header1")
        self.section_seperator3.setObjectName("separator3")
        self.section_seperator2.setObjectName("separator2")
        self.section_seperator1.setObjectName("separator1")
        #-----------------------



        #create layout
        self.sections_layout=QVBoxLayout(self)
        self.customization_content=self.settings_customization()
        self.notification_content=self.settings_notification()
        self.data_content=self.settings_data()
        self.sections_layout.addWidget(self.customization_header,20)
        self.sections_layout.addWidget(self.section_seperator1,10)
        self.sections_layout.addLayout(self.customization_content)
        self.sections_layout.addWidget(self.notification_header,20)
        self.sections_layout.addWidget(self.section_seperator2,10)
        self.sections_layout.addLayout(self.notification_content)
        self.sections_layout.addWidget(self.data_header,20)
        self.sections_layout.addWidget(self.section_seperator3,10)
        self.sections_layout.addLayout(self.data_content)
        self.main_layout=QVBoxLayout()
        self.scroll_area=QScrollArea(self)
        self.scroll_area.setLayout(self.sections_layout)
        self.scroll_area.setWidgetResizable(True)
        self.main_layout.addWidget(self.scroll_area)
        self.main_layout.setContentsMargins(0,0,0,0)
        self.setContentsMargins(0,0,0,0)
        self.setLayout(self.main_layout)
        self.setStyleSheet("""
    QLabel#separator1{
        border : solid black;
        border-width : 5px 0px 0px 0px;
    }
    QLabel#separator2{
        border : solid black;
        border-width : 5px 0px 0px 0px;
    }
    QLabel#separator3{
        border : solid black;
        border-width : 5px 0px 0px 0px;
    }
    QLabel#header1{
        font:30px;
        font-family: Arial;
    }
    QLabel#header2{
        font:30px;
        font-family: Arial;
    }
    QLabel#header3{
        font:30px;
        font-family: Arial;
    }
    """)
        #--------
    #create customization layout
    def settings_customization(self):

        #create buttons and texts
        self.change_theme_button=QPushButton("Change Theme",self)
        self.change_font_button=QPushButton("Change font",self)
        self.select_font=QComboBox(self)
        self.select_font_size=QComboBox(self)
        self.select_font.addItem("Arial")
        self.select_font_size.addItem("10")
        self.font_text=QLabel("Font : ",self)
        #------------------------

        #create main widget and main layout
        self.grid=QGridLayout(self)
        self.grid.addWidget(self.font_text,0,0)
        self.grid.addWidget(QLabel("",self),0,1)
        self.grid.addWidget(self.select_font,0,2,1,2)
        self.grid.addWidget(self.select_font_size,0,4)
        self.grid.addWidget(self.change_font_button,0,5,1,2)
        self.grid.addWidget(self.change_theme_button,1,0,1,7)
        #----------------------------------

        
        return self.grid
    
    #create data layout
    def settings_data(self):

        #create buttons and texts
        self.delete_all_apps_data=QPushButton("Delete all data",self)
        self.delete_all_users_data=QPushButton("Delete all users data",self)
        #------------------------

        #create main widget and main layout
        
        self.grid2=QGridLayout(self)
        self.grid2.addWidget(self.delete_all_users_data,0,0)
        self.grid2.addWidget(self.delete_all_apps_data,0,1)
        #----------------------------------

        
        return self.grid2
    
    
    def delete_all_users(self):
        query1=QSqlQuery()
        query1.prepare("""DROP TABLE IF EXISTS User """)
        query1.exec_()


    #connecting the buttons
    def connect_buttons(self,tabs,database):
        self.change_theme_button.clicked.connect(lambda : tabs.setCurrentIndex(3))
        self.database=database
        self.delete_all_users_data.clicked.connect(self.delete_all_users)
        self.delete_all_apps_data.clicked.connect(self.delete_all_data)
    #---------------------
        
    def delete_all_data(self):
        query1=QSqlQuery()
        query1.prepare("""DROP TABLE IF EXISTS User """)
        query1.exec_()
        query2=QSqlQuery()
        query2.prepare("""DROP TABLE IF EXISTS Data """)
        query2.exec_()
    #create notification layout
    def settings_notification(self):

        #create buttons and texts
        self.change_sending_time_text=QLabel("Change sending time : ",self)
        self.change_sending_time_button=QTimeEdit(self)
        self.change_sending_time_submit_button=QPushButton("Change time",self)
        #------------------------

        #create main widget and main layout
        
        self.grid1=QGridLayout(self)
        self.grid1.addWidget(self.change_sending_time_text,0,0,1,2)
        self.grid1.addWidget(self.change_sending_time_button,0,5,1,2)
        self.grid1.addWidget(self.change_sending_time_submit_button,1,0,1,7)
        self.change_sending_time_submit_button.clicked.connect(self.change_notif_sending_time)
        #----------------------------------

        
        return self.grid1
    #change notification time
    def change_notif_sending_time(self):  
        time = self.change_sending_time_button.time()  
        time2 = time.hour()
        check_time.set_notification_time(self.database,time2)     
class setting_customization_tab(QWidget):
    def __init__(self):
        super().__init__()
        self.tab2 = self.create_main_tab()
    def create_main_tab(self):
        self.FontColor = QComboBox(self)
        self.tab1_main_layout=QVBoxLayout(self)
        self.tab1_header_layout=QGridLayout(self)
        self.tab1_button_layout=QHBoxLayout(self)
        self.tab1_group_button_layout = QHBoxLayout(self)
        self.appply_button=QPushButton("Apply",self)
        self.cancel_button=QPushButton("Cancel",self)
        self.back_button=QPushButton("",self)
        self.buton_color = QComboBox(self)
        self.background = QComboBox(self)
        self.buton_color.addItems(["DarkGreen","DarkBlue","Lightgreen","LightBlue","Yellow","Orange","Lightred","Darkpurple"])
        self.background.addItems(["White","Gray","Dark","Olive","Darkpurple"])
        self.FontColor.addItems(["White","Black"])
        self.tab1_group_button_layout.addWidget(QLabel("Button Color : "))
        self.tab1_group_button_layout.addWidget(self.buton_color)
        self.tab1_group_button_layout.addWidget(QLabel("Background Color : "))
        self.tab1_group_button_layout.addWidget(self.background)
        self.tab1_group_button_layout.addWidget(QLabel("Font Color : "))
        self.tab1_group_button_layout.addWidget(self.FontColor)
        self.back_button.setIcon(QIcon('C:/Users/r/Contacts/Desktop/9thgrade_project/assets/back.png'))
        size=QSize(40,40)
        self.back_button.setIconSize(size)
        self.header=QLabel("Change Theme",self)
        self.back_button.setObjectName("back_button")
        self.tab1_header_layout.addWidget(self.back_button,0,0)
        self.tab1_header_layout.addWidget(QLabel("",self),0,1)
        self.tab1_header_layout.addWidget(QLabel("",self),0,2)
        self.tab1_header_layout.addWidget(QLabel("",self),0,3)
        self.tab1_header_layout.addWidget(QLabel("",self),0,4)
        self.tab1_header_layout.addWidget(self.header,0,5,1,2)
        self.header.setAlignment(Qt.AlignRight)
        self.tab1_button_layout.addWidget(self.appply_button)
        self.tab1_button_layout.addWidget(self.cancel_button)
        self.tab1_main_layout.addLayout(self.tab1_header_layout,10)
        self.tab1_main_layout.addLayout(self.tab1_group_button_layout,60)
        self.tab1_main_layout.addLayout(self.tab1_button_layout,10)
        self.back_button.setMaximumSize(50,50)
        

        self.setLayout(self.tab1_main_layout)
        self.setStyleSheet("""
    QPushButton#back_button{
        padding: 25px 25px 25px 25px;
        background: transparent;
    }
    """)
    
    
    #connecting the buttons
    def connect_buttons(self,tabs,widget):
        self.back_button.clicked.connect(lambda : tabs.setCurrentIndex(2))
        self.cancel_button.clicked.connect(lambda : tabs.setCurrentIndex(2))
    #---------------------
