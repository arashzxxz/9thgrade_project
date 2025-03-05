
import sys
import requests
import os
from assets.assests import get_assets_working_dir
from users import current_user
from datetime import datetime
from calculations import check_time
from calculations.calculations import string_to_list
from data.check_streak import check_decreased
from ui.main_tab import exercise_tabs,schedules_tab,food_suggestion
from ui import Menu, Settings_Tab, log_in_and_sign_in,styles,chart_widget
from ui.main_tab import calendar_widget,main_widget,timer,log_in_error
from PyQt5.QtSql import QSqlDatabase,QSqlQuery
from PyQt5.QtWidgets import QApplication,QColorDialog,QMainWindow,QMessageBox,QTabWidget, QWidget,QFileDialog, QLabel,QListWidget ,QComboBox,QPushButton ,QVBoxLayout,QTableWidget,QVBoxLayout,QHBoxLayout
from PyQt5.QtGui import QIcon
from data.update_streak import update_button
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
        check_decreased(self.database,datetime.today())
        #update_button(self.database)
        check_time.start_background_task_undone(self.database)
        check_time.start_background_task_notification(self.database, 12)
        #--------------------------------------------

    # Create database tables  
    def create_db_tables(self):  
        query_user = '''  
            CREATE TABLE IF NOT EXISTS User (  
                user_id INTEGER PRIMARY KEY,  
                username VARCHAR NOT NULL,  
                password VARCHAR,  
                streak INTEGER DEFAULT 0,
                last_day_online VARCHAR,
                freeze INTEGER DEFAULT 0,
                last_day_streak VARCHAR,
                FOREIGN KEY (user_id) REFERENCES Data(id)  
                ON UPDATE NO ACTION ON DELETE CASCADE  
            );  
        '''  


        query_data = '''  
            CREATE TABLE IF NOT EXISTS Data (  
                id INTEGER NOT NULL,  
                weight INTEGER,  
                height INTEGER,  
                age INTEGER,  
                gender VARCHAR,
                days TEXT,
                start_date TEXT,
                end_date TEXT,
                data_days_state BLOB,
                number INTEGER,
                name VARCHAR,
                data_days_calories BLOB,
                data_days_workout BLOB,
                bmi INTEGER,
                ideal_weight INTEGER,
                calories_per_day INTEGER
            );  
        '''   

        query = QSqlQuery()  
        if not query.exec_(query_user):  
            QMessageBox.critical(None, "Error", "Could not create User table: " + query.lastError().text())  
        if not query.exec_(query_data):  
            QMessageBox.critical(None, "Error", "Could not create Data table: " + query.lastError().text())  

    #open the data bases
    def get_data_base(self):  
        self.database = QSqlDatabase.addDatabase("QSQLITE")
        self.database.setDatabaseName("Database.db")                    
        if not self.database.open():  
            QMessageBox.critical(None, "Error", "Could not open the database: " + self.database.lastError().text())  
            sys.exit(1)  
        #------------------
        

    #connect all of the buttons
    def connect_all_buttons(self):
        self.main_menu.connect_buttons(self.tabs,self.main_tab_schedules,self.chart_tab)
        self.settings_tab.connect_buttons(self.tabs,self.database)#incomplete
        self.settings_customization_tab.connect_buttons(self.tabs)
        self.log_in_and_sign_in_tab.connect_buttons(self.tabs,self.database)
        self.main_tab.connect_buttons(self.tabs,self.database,self.main_tab.calendar_widget)
        self.exercise_tab.timer_widget.connect_buttons()
        self.exercise_tab.connect_buttons(self.tabs)
        self.main_tab_schedules.connect_buttons(self.tabs)
        self.food_suggestion_tab.connect_buttons(self.tabs)
        self.main_tab_schedules.expand_button.clicked.connect(self.expand_current_schedules_days)
        self.main_tab.backbutton.clicked.connect(self.main_tab_schedules.load_schedule_days)
    #-------------------------
    
    def expand_current_schedules_days(self):
        query_schedule_info = QSqlQuery()  
        data_id = current_user.logged_in_user.data_id
        selected_schedule = current_user.logged_in_user.selected_schedule
        # print(data_id)
        # print(selected_schedule)
        query_schedule_info.prepare("""SELECT * FROM Data WHERE id = ? and number = ?""")  
        query_schedule_info.addBindValue(data_id)  
        query_schedule_info.addBindValue(selected_schedule)  
        query_schedule_info.exec_()  
        if query_schedule_info.exec_():
            pass
            if query_schedule_info.next():
                pass
        needed_calories = query_schedule_info.value(15)
        list_status = string_to_list(query_schedule_info.value(8))
        self.main_tab.current_day_content1.needed_calories_text2.setText(str(needed_calories))
        self.tabs.setCurrentIndex(0)
        self.main_tab.calendar_widget.create_calendar_buttons()

    def initui(self):
        #create all of the main tabs
        get_assets_working_dir()
        self.chart_tab = chart_widget.Chart_Widget(database = self.database)
        self.main_tab=main_widget.Main_widget()
        self.main_tab_schedules=schedules_tab.SchedulesTab()
        self.main_tab_schedules.get_database(database=self.database)
        self.content_tab2=self.createtab2()
        self.exercise_tab=exercise_tabs.Exercise_tab()
        self.food_suggestion_tab=food_suggestion.Food_suggestions()
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
        self.tabs.addTab(self.food_suggestion_tab,"")
        self.tabs.addTab(self.chart_tab,"")
        self.tabs.setStyleSheet('''QTabBar::tab{width: 0;height: 0; margin: 0; padding: 0; border: none;}''')
        self.tabs.setCurrentIndex(6)
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