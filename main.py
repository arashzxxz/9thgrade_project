
import sys
import requests
import os
from users import current_user
from ui.main_tab import exercise_tabs,schedules_tab
from ui import Menu, Settings_Tab, log_in_and_sign_in,styles
from ui.main_tab import calendar_widget,main_widget,timer,log_in_error
from PyQt5.QtSql import QSqlDatabase,QSqlQuery
from PyQt5.QtCore import Qt,QTime,QTimer,QDate,QSize
from PyQt5.QtWidgets import QApplication,QColorDialog,QMainWindow,QScrollArea,QStyleFactory,QStackedWidget,QTreeView,QDateEdit,QTableWidgetItem,QMessageBox,QTabWidget, QWidget,QFileDialog, QLabel,QListWidget ,QComboBox,QPushButton ,QVBoxLayout,QTableWidget,QVBoxLayout,QHBoxLayout,QGridLayout,QCheckBox,QRadioButton,QButtonGroup,QLineEdit
from PyQt5.QtGui import QIcon,QFont,QPixmap,QFontDatabase,QStandardItemModel,QStandardItem
class mainw(QMainWindow):
    def __init__(self):
        #create main window
        super(mainw,self).__init__()
        self.setWindowTitle('FitLife')
        self.setWindowIcon(QIcon("C:/Users/r/Contacts/Desktop/9thgrade_project/assets/logo.png"))
        self.Width = 1000
        self.height = int(0.618 * self.Width)
        self.resize(self.Width, self.height)
        #------------------

        #call the gdb function and setup the data structure
        self.get_data_base()
        self.create_db_tables()
        #---------------------------------------------------


        #create tabs and menus and connecting buttons
        self.initui()
        self.connect_all_buttons()
        #--------------------------------------------

    # Create database tables  
    def create_db_tables(self):  
        query_user = '''  
            CREATE TABLE IF NOT EXISTS User (  
                id INTEGER PRIMARY KEY AUTOINCREMENT,  
                username VARCHAR NOT NULL,  
                password VARCHAR,  
                data_id INTEGER,  
                PRIMARY KEY(id),  
                FOREIGN KEY (data_id) REFERENCES Data(id)  
                ON UPDATE NO ACTION ON DELETE NO ACTION  
            );  
        '''  

        query_data = '''  
            CREATE TABLE IF NOT EXISTS Data (  
                id INTEGER NOT NULL UNIQUE,  
                weight NUMERIC,  
                height INTEGER,  
                bmi NUMERIC,  
                PRIMARY KEY(id)  
            );  
        '''   

        query = QSqlQuery()  
        if not query.exec_(query_user):  
            QMessageBox.critical(None, "Error", "Could not create User table: " + query.lastError().text())  
        if not query.exec_(query_data):  
            QMessageBox.critical(None, "Error", "Could not create Data table: " + query.lastError().text())  

    #----------------


    #open the data bases
    def get_data_base(self):  
        self.database = QSqlDatabase.addDatabase("QSQLITE")
        self.database.setDatabaseName("database.db")                    
        if not self.database.open():  
            QMessageBox.critical(None, "Error", "Could not open the database: " + self.database.lastError().text())  
            sys.exit(1)  
        #------------------
        

    #connect all of the buttons
    def connect_all_buttons(self):
        self.main_menu.connect_buttons(self.tabs)
        self.settings_tab.connect_buttons(self.tabs)#incomplete
        self.settings_customization_tab.connect_buttons(self.tabs)
        self.log_in_and_sign_in_tab.connect_buttons(self.tabs,self.database)
        self.main_tab.connect_buttons(self.tabs)
        self.exercise_tab.timer_widget.connect_buttons()
        self.exercise_tab.connect_buttons()
        self.main_tab_schedules.connect_buttons(self.tabs)
    #-------------------------


    def initui(self):
        #create all of the main tabs
        self.main_tab=main_widget.Main_widget()
        self.main_tab_schedules=schedules_tab.SchedulesTab()
        self.content_tab2=self.createtab2()
        self.exercise_tab=exercise_tabs.Exercise_tab()
        self.settings_tab=Settings_Tab.setting_tab()
        self.settings_tab.setObjectName("settings_tab")
        self.settings_customization_tab=Settings_Tab.setting_customization_tab()
        self.log_in_and_sign_in_tab=log_in_and_sign_in.connect_pages()
        self.main_tab_log_in_error_tab=log_in_error.Log_in_error_tab()
        #---------------------------

        #connect all of the tabs
        self.tabs=QTabWidget()
        self.tabs.addTab(self.main_tab,"")
        self.tabs.addTab(self.content_tab2,"")
        self.tabs.addTab(self.settings_tab,"")
        self.tabs.addTab(self.settings_customization_tab,"")
        self.tabs.addTab(self.log_in_and_sign_in_tab,"")
        self.tabs.addTab(self.exercise_tab,"")
        self.tabs.addTab(self.main_tab_log_in_error_tab,"")
        self.tabs.addTab(self.main_tab_schedules,"")
        self.tabs.setStyleSheet('''QTabBar::tab{width: 0;height: 0; margin: 0; padding: 0; border: none;}''')
        self.tabs.setCurrentIndex(7)
        #-----------------------


        #create main layout and menu
        self.main_layout=QHBoxLayout(self)
        self.main_menu=Menu.Menu()
        self.main_layout.addWidget(self.main_menu,0)
        self.main_layout.addWidget(self.tabs,1)
        self.main_layout.setContentsMargins(0,0,0,0)
        self.main_widget=QWidget()
        self.main_widget.setLayout(self.main_layout)
        self.setCentralWidget(None)
        self.setCentralWidget(self.main_widget)
        self.main_menu.home_button.setChecked(True) 
        #---------------------------

        #style all of the app
        self.set_styles()
        #-------------------

    #test tab
    def createtab2(self):
        vb1=QVBoxLayout()
        vb1.addWidget(QPushButton("2",self))
        gui=QWidget()
        gui.setLayout(vb1)
        return gui
    #--------

    #set the styles
    def set_styles(self):
        # self.setStyleSheet(styles.style_sheets.main_style)
        self.main_menu.setStyleSheet(styles.style_sheets.menu_style)
        # self.main_widget.setStyleSheet(styles.style_sheets.main_style)
    #-------------


def main():
    app=QApplication(sys.argv)
    window=mainw()
    window.show()
    sys.exit(app.exec_())
if __name__ == "__main__":
    main()