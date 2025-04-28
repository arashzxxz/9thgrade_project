import sys
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
from PyQt5.QtWidgets import QApplication,QMainWindow,QMessageBox,QTabWidget, QWidget,QFileDialog, QLabel,QListWidget ,QComboBox,QPushButton ,QVBoxLayout,QTableWidget,QVBoxLayout,QHBoxLayout
from PyQt5.QtGui import QIcon
class mainw(QMainWindow):
    def __init__(self):
        #create main window
        super(mainw,self).__init__()
        self.setWindowTitle('FitLife')
        self.setWindowIcon(QIcon(get_assets_working_dir() + "/logo.png"))
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
        self.main_menu.home_button.setChecked(1)
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
                calories_per_day INTEGER,
                carbohydrates INTEGER,
                protein INTEGER,
                fat INTEGER
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
            
    def get_streak(self):
        query1=QSqlQuery()
        query1.prepare("""SELECT * FROM User WHERE username = ? AND password = ?""")
        query1.addBindValue(current_user.logged_in_user.username)
        query1.addBindValue(current_user.logged_in_user.password)
        query1.exec_()
        a = query1.value(6)
        if a == datetime.today() : 
            self.main_menu.streak_button.setStyleSheet("""
                QRadioButton#streakb::indicator::unchecked{
                                image: url(""" + get_assets_working_dir() + """/streak_done.png);
                                
                }
                QRadioButton#streakb::indicator::checked{
                                image: url(""" + get_assets_working_dir() + """/streak_done.png);
                                
                }""")  
        if query1.value(3) == 10:
            query_freeze = QSqlQuery()  
            query_freeze.prepare("""UPDATE User SET freeze = ? WHERE username = ? AND password = ?""")  
            if not current_user.logged_in_user.freeze:
                current_user.logged_in_user.freeze=0
            query_freeze.addBindValue(current_user.logged_in_user.freeze + 1)  
            query_freeze.addBindValue(current_user.logged_in_user.username)  
            query_freeze.addBindValue(current_user.logged_in_user.password)          
            query_freeze.exec_()

    #connect all of the buttons
    def connect_all_buttons(self):
        self.main_menu.connect_buttons(self.tabs,self.main_tab_schedules,self.chart_tab)
        self.settings_tab.connect_buttons(self.tabs,self.database)#incomplete
        self.settings_customization_tab.connect_buttons(self.tabs,self)
        self.log_in_and_sign_in_tab.connect_buttons(self.tabs,self.database,self.main_menu.streak_button)
        self.main_tab.connect_buttons(self.tabs,self.database,self.main_tab.calendar_widget,self.main_menu.streak_button)
        self.exercise_tab.timer_widget.connect_buttons()
        self.exercise_tab.connect_buttons(self.tabs)
        self.main_tab_schedules.connect_buttons(self.tabs)
        self.food_suggestion_tab.connect_buttons(self.tabs)
        self.main_tab_schedules.expand_button.clicked.connect(self.expand_current_schedules_days)
        self.main_tab.backbutton.clicked.connect(self.main_tab_schedules.load_schedule_days)
        self.settings_customization_tab.appply_button.clicked.connect(lambda : self.set_all_styles(self.settings_customization_tab.background.currentText(),self.settings_customization_tab.buton_color.currentText(),self.settings_customization_tab.FontColor.currentText()))
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
        self.food_suggestion_tab.change_suggestions(query_schedule_info.value(17),query_schedule_info.value(16),query_schedule_info.value(18))

    def initui(self):
        #create all of the main tabs
        get_assets_working_dir()
        self.chart_tab = chart_widget.Chart_Widget(database = self.database)
        self.main_tab=main_widget.Main_widget()
        self.main_tab_schedules=schedules_tab.SchedulesTab()
        self.main_tab_schedules.get_database(database=self.database)
        self.exercise_tab=exercise_tabs.Exercise_tab()
        self.food_suggestion_tab=food_suggestion.Food_suggestions()
        self.settings_tab=Settings_Tab.setting_tab(self.database)
        self.settings_tab.setObjectName("settings_tab")
        self.settings_customization_tab=Settings_Tab.setting_customization_tab()
        self.log_in_and_sign_in_tab=log_in_and_sign_in.connect_pages()
        self.main_tab_log_in_error_tab=log_in_error.Log_in_error_tab()
        #---------------------------

        #connect all of the tabs
        self.tabs=QTabWidget()
        self.tabs.addTab(self.main_tab,"")
        self.tabs.addTab(QWidget(self),"")
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
        self.main_tab_schedules.delete_radio_button.setObjectName("deleterb")
        self.main_menu.setStyleSheet(styles.style_sheets.menu_style)
        self.get_theme()
        #-------------------
    def get_theme(self):  
        with open("theme.txt", "r") as f:  
            lines = f.readlines()  
            background = lines[0].strip()  
            button = lines[1].strip()  
            font = lines[2].strip()  
            self.set_all_styles(background,button,font)  

    def save_theme(self, background, button, font):  
        with open("theme.txt", "w") as f:  
            f.writelines([background + "\n", button + "\n", font + "\n"])  

    def set_all_styles(self,background,button,font):
        b1=""
        b2=""
        bg1=""
        bg2=""
        fc=font
        background_colors = {  
            "White": ("#cfcfcf", "#a3a3a2"),  
            "Gray": ("#2e2e2e", "#242423"),  
            "Dark": ("#121212", "#000000"),  
            "Olive": ("#1a200e", "#273013"),
            "Darkpurple": ("#240020","#380132") 
        }  

        button_colors = {  
            "DarkGreen": ("#014d02", "#013d03"),  
            "DarkBlue": ("#0b0e29", "#080b21"),  
            "Lightgreen": ("#27a32b", "#48cf13"),  
            "LightBlue": ("#117e96", "#1aa7c7"),  
            "Yellow": ("#d9ad1c", "#f5e616"),  
            "Orange": ("#d65900", "#ff8800"),
            "Lightred": ("#eb4034", "#992b23"),
            "Darkpurple": ("#3c0b4d","#220436")
        }  

        bg1, bg2 = background_colors.get(background, (None, None))  
        b1, b2 = button_colors.get(button, (None, None))  
        self.setStyleSheet("""  
            QWidget { background-color: """+bg1+"""; color: """+fc+"""; font-size: 16px;}  
            QPushButton { color: """+fc+"""; border-radius: 10px; padding: 10px; background-color: """+b1+""";}  
            QLabel { color: """+fc+"""; }  
            QLineEdit { background-color: """+bg1+"""; color: """+fc+"""; border-radius: 5px; padding: 5px; }  
            QComboBox { background-color: """+bg1+"""; color: """+fc+"""; border-width: 2px; border-style: solid; border-color: """+b1+""";}  
            QScrollBar:vertical { background: """+bg1+"""; width: 10px; }  
            QScrollBar::handle:vertical { min-height: 20px; border-radius: 5px; background: """+b1+"""; }  
            QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical { background: """+bg1+"""; }  
            QLineEdit {border-radius: 5px; border-color: """+fc+"""; border-width: 2px; border-style: solid; }
            QLineEdit::hover {background: """+bg2+"""; } 
            QComboBox::hover { background: """+bg2+"""; }
            QPushButton::hover {background: """+b2+"""; }
            QRadioButton#deleterb::indicator {border-color: """+b1+""";background-color: """+bg1+"""; color: """+fc+"""; border-width: 2px; border-style: solid;}
            QTimeEdit {border-radius: 5px; border-width: 2px; border-style: solid;border-color: """+b1+""";}
            QRadioButton#deleterb::indicator::checked {background-color: #540000; }
            QRadioButton#deleterb::indicator::hover {background-color: #360000; }
            QTimeEdit::drop-down::hover {background: """+b2+"""; }  
            QTimeEdit::drop-down {border-color: """+b1+""";border-radius: 5px; border-width: 2px; border-style: solid;}  
            QPushButton:pressed {margin: 2px 4px 4px 2px;}
            QRadioButton:pressed {margin: 4px 4px 4px 4px;}     
        """)  
        self.save_theme(background,button,font)



def main():
    app=QApplication(sys.argv)
    window=mainw()
    window.show()
    sys.exit(app.exec_())
if __name__ == "__main__":
    main()