import sys 
from PyQt5.QtWidgets import QApplication,QColorDialog,QMainWindow,QScrollArea,QStyleFactory,QStackedWidget,QTreeView,QDateEdit,QTableWidgetItem,QMessageBox,QTabWidget, QWidget,QFileDialog, QLabel,QListWidget ,QComboBox,QPushButton ,QVBoxLayout,QTableWidget,QVBoxLayout,QHBoxLayout,QGridLayout,QCheckBox,QRadioButton,QButtonGroup,QLineEdit
from PyQt5.QtCore import Qt, QDate  
from PyQt5.QtSql import QSqlDatabase,QSqlQuery
from users import current_user
from datetime import datetime,timedelta
from calculations.calculations import string_to_list,list_to_string
import main
from data.check_streak import check_increased
from ui.main_tab import calendar_widget,current_day_content
from assets.assests import get_assets_working_dir
    

class Main_widget(QWidget):  
    def __init__(self):  
        super().__init__()  
        # create the layouts
        self.current_day_content=QVBoxLayout()
        self.main_layout=QHBoxLayout()
        self.top_buttons_layout=QHBoxLayout()
        #-------------------

        #add the widgets
        self.calendar_widget=calendar_widget.Calendar_widget()
        self.calendar_widget.get_main_widget(self)
        self.current_day_content1=current_day_content.Current_day_food_widget()
        self.current_day_content2=current_day_content.Current_day_exercise_widget()
        self.submit_button = QPushButton("Submit",self)
        self.date=QLabel("Dec 4, 2024",self)
        self.date.setStyleSheet("font-size: 20px")
        self.date.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.date.setText(str(datetime.today().strftime("%Y / %m / %d")))
        self.backbutton=QPushButton("",self)
        self.backbutton.setStyleSheet("background-color: transparent; border-radius: 0px; image: url("+get_assets_working_dir()+"back.png)")
        self.top_buttons_layout.addWidget(self.backbutton,1)
        self.top_buttons_layout.addWidget(self.date,3)
        self.current_day_content.addLayout(self.top_buttons_layout,10)
        self.current_day_content.addWidget(self.current_day_content1,60)
        self.current_day_content.addWidget(self.current_day_content2,30)
        self.main_layout.addWidget(self.calendar_widget,30)
        self.current_day_content.addWidget(self.submit_button,10)
        self.main_layout.addLayout(self.current_day_content,70)
        #---------------

        #set the layout
        self.setLayout(self.main_layout)
        #self.set_stylesheet()
        #--------------

    #connect all the buttons
    def connect_buttons(self,tabs,data_base,clender_widget,button):
        self.calendar_widget.get_data_base(data_base)
        self.current_day_content2.expand_button.clicked.connect(lambda : tabs.setCurrentIndex(5))
        self.current_day_content1.expand_button.clicked.connect(lambda : tabs.setCurrentIndex(8))
        self.backbutton.clicked.connect(lambda : tabs.setCurrentIndex(7))
        self.submit_button.clicked.connect(lambda : self.submit_current_day_data(data_base,clender_widget,button))
    #-----------------------

    def submit_current_day_data(self,data_base,clender_widget,button):
        eaten_calories = int(self.current_day_content1.eaten_calories_entry.text())
        workout_time = int(self.current_day_content2.workout_time_entry.text())
        query1 = QSqlQuery()
        query1.prepare("""SELECT * FROM Data WHERE id = ? and number = ?""")  
        query1.addBindValue(current_user.logged_in_user.data_id)  
        query1.addBindValue(current_user.logged_in_user.selected_schedule)  
        query1.exec_()  
        if query1.exec_():
            pass
            if query1.next():
                pass
        calories_per_day = int(query1.value(15))
        if calories_per_day-(calories_per_day//10) < eaten_calories < calories_per_day+(calories_per_day//10) :
            status = "perfect"
        else : 
            status = "done"
        current_date = datetime.today()
        first_date = query1.value(6)
        first_date = datetime.strptime(first_date, "%Y-%m-%d") 
        list_status = string_to_list(query1.value(8))
        list_calories = string_to_list(query1.value(11))
        list_workout = string_to_list(query1.value(12))
        day = current_date - first_date
        list_status[day.days] = status
        list_calories[day.days] = eaten_calories
        list_workout[day.days] = workout_time

        query_update = QSqlQuery()  
        query_update.prepare("""UPDATE data SET data_days_state = ? , data_days_calories = ? ,data_days_workout = ? WHERE id = ? AND number = ?""")  
        query_update.addBindValue(list_to_string(list_status))
        query_update.addBindValue(list_to_string(list_calories))
        query_update.addBindValue(list_to_string(list_workout))
        query_update.addBindValue(current_user.logged_in_user.data_id)
        query_update.addBindValue(current_user.logged_in_user.selected_schedule)
        query_update.exec_() 
        clender_widget.create_calendar_buttons()
        check_increased(data_base,current_date,day.days,button)
    def clear_main_layout(self):  
        while self.main_layout.count():  
            item = self.main_layout.takeAt(0)  # Get the first item  
            if item.widget():  # If it's a widget, remove it from the layout  
                self.main_layout.removeWidget(item.widget())  
                item.widget().hide()  # Optionally hide the widget  
            else:  # If it's a layout, remove it  
                self.main_layout.removeItem(item)  

    def set_mode_undone(self):  
        print("aaaaaaaaaaaaaaaaaaaaa")
        self.clear_main_layout()  
        icon_label = QLabel("")  
        icon_label.setStyleSheet("background-color: transparent; image: url("+get_assets_working_dir()+"undone.png);")  
        text_label = QLabel("You didn't do your diet")  
        undone_layout = QHBoxLayout()  
        undone_layout.addWidget(icon_label)  
        undone_layout.addWidget(text_label)  
        self.main_layout.addWidget(self.calendar_widget)  
        self.calendar_widget.show()
        self.main_layout.addLayout(undone_layout)  

    def set_mode_done(self):  
        self.clear_main_layout()  
        icon_label = QLabel("")  
        icon_label.setStyleSheet("background-color: transparent; image: url("+get_assets_working_dir()+"done.png);")  
        text_label = QLabel("nice")  
        done_layout = QHBoxLayout()  
        done_layout.addWidget(icon_label)  
        done_layout.addWidget(text_label)  
        self.main_layout.addWidget(self.calendar_widget)  
        self.calendar_widget.show()
        self.main_layout.addLayout(done_layout)  

    def set_mode_perfect(self):  
        self.clear_main_layout()  
        icon_label = QLabel("")  
        icon_label.setStyleSheet("background-color: transparent; image: url("+get_assets_working_dir()+"perfect.png);")  
        text_label = QLabel("great job!")  
        perfect_layout = QHBoxLayout()  
        perfect_layout.addWidget(icon_label)  
        perfect_layout.addWidget(text_label)
        self.main_layout.addWidget(self.calendar_widget)  
        self.calendar_widget.show()  
        self.main_layout.addLayout(perfect_layout)  

    def set_mode_none(self):  
        self.clear_main_layout()  
        self.main_layout.addWidget(self.calendar_widget)  
        self.calendar_widget.show()
        self.main_layout.addLayout(self.current_day_content)  
        self.date.setText(str(datetime.today().strftime("%Y / %m / %d")))  

        query_schedule_info = QSqlQuery()  
        data_id = current_user.logged_in_user.data_id  
        selected_schedule = current_user.logged_in_user.selected_schedule  
        query_schedule_info.prepare("""SELECT * FROM Data WHERE id = ? and number = ?""")  
        query_schedule_info.addBindValue(data_id)  
        query_schedule_info.addBindValue(selected_schedule)  
        query_schedule_info.exec_()  
        if query_schedule_info.exec_():  
            if query_schedule_info.next():  
                needed_calories = query_schedule_info.value(15)  
                self.current_day_content1.needed_calories_text2.setText(str(needed_calories))
        
    def set_stylesheet(self):  
        self.setStyleSheet("""  
            QWidget { background-color: #1c1c1c; color: white; }  
            QPushButton { background-color: #014d02; color: white; border-radius: 10px; padding: 10px; }  
            QLabel { color: white; }  
            QLineEdit { background-color: #1c1c1c; color: white; border-radius: 5px; padding: 5px; }  
            QComboBox { background-color: #1c1c1c; color: white; border-radius: 5px; }  
            QScrollBar:vertical { background: #1c1c1c; width: 10px; }  
            QScrollBar::handle:vertical { background: #014d02; min-height: 20px; border-radius: 5px; }  
            QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical { background: #1c1c1c; }  
        """)  