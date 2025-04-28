import sys  
import hashlib as hash
import re
from assets.assests import get_assets_working_dir
from calculations import calculations as cal
from datetime import date,timedelta,datetime
from PyQt5.QtSql import QSqlDatabase,QSqlQuery
from users import current_user
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget,  
                             QVBoxLayout, QHBoxLayout, QRadioButton,  
                             QPushButton, QGroupBox, QScrollArea,  
                             QFrame, QDialog, QLabel, QLineEdit ,QComboBox,QGridLayout)  

class DayButton(QPushButton):
    def __init__(self,name,date,state):  
        super().__init__(name)  
        self.date=date
        self.state=state

class ScheduleButton(QPushButton):
    def __init__(self,name,number):  
        super().__init__(name)  
        self.button_number=number
class UserInputDialog(QDialog):  
    def __init__(self):  
        super().__init__()  
        self.setWindowTitle("User Details")  
        self.setGeometry(200, 200, 350, 250)   
        self.layout = QVBoxLayout()  
        
        self.name_input = QLineEdit(self)  
        self.name_input.setPlaceholderText("Schedule's name")      
        self.days_input = QLineEdit(self)  
        self.days_input.setPlaceholderText("How long is this schedule?")     
        self.weight_input = QLineEdit(self)  
        self.weight_input.setPlaceholderText("Weight (in kg)")  
        self.height_input = QLineEdit(self)  
        self.height_input.setPlaceholderText("Height (in cm)")  
        self.age_input = QLineEdit(self)  
        self.age_input.setPlaceholderText("Age")  
        
        self.gender_male = QRadioButton("male")  
        self.gender_female = QRadioButton("female")  

        self.submit_button = QPushButton("Submit", self)  
        self.submit_button.clicked.connect(self.submit_data)  
        
        self.layout.addWidget(QLabel("Name:"))  
        self.layout.addWidget(self.name_input)  
        self.layout.addWidget(QLabel("Weight (kg):"))  
        self.layout.addWidget(self.weight_input)  
        self.layout.addWidget(QLabel("Height (cm):"))  
        self.layout.addWidget(self.height_input)  
        self.layout.addWidget(QLabel("Age:"))  
        self.layout.addWidget(self.age_input)  

        self.layout.addWidget(QLabel("Gender:"))   
        self.gender_layout=QHBoxLayout()
        self.gender_layout.addWidget(self.gender_male)
        self.gender_layout.addWidget(self.gender_female)
        self.layout.addLayout(self.gender_layout)

        self.layout.addWidget(QLabel("Number of days:"))  
        self.layout.addWidget(self.days_input)   
        self.setLayout(self.layout)  
        self.Schedule_name = None  
        self.gender = ""
        self.gender_male.clicked.connect(self.set_gender)
        self.gender_female.clicked.connect(self.set_gender)

        self.activity_level_combo = QComboBox()  
        self.activity_level_combo.addItems([  
            "sedentary", "lightly_active", "moderately_active",   
            "very_active", "super_active"  
        ])  
        self.layout.addWidget(self.activity_level_combo)  
        self.layout.addWidget(self.submit_button) 
    def set_gender(self):  
        if self.gender_male.isChecked():  
            self.gender = "male"  
        elif self.gender_female.isChecked():  
            self.gender = "female"  

    def submit_data(self):  
        name = self.name_input.text()  
        self.Schedule_name = name   
        self.activity_level = self.activity_level_combo.currentText()
        self.accept()

    def get_button_name(self):  
        return self.Schedule_name


class SchedulesTab(QMainWindow):  
    def __init__(self):  
        super().__init__()  
        self.setWindowTitle("Push Buttons Scroll Example")  
        self.setGeometry(100, 100, 600, 300)  
        self.main_widget = QWidget(self)  
        self.setCentralWidget(self.main_widget)  
        self.layout = QHBoxLayout()   
        self.main_layout = QVBoxLayout()  
        self.main_widget.setLayout(self.layout)  
        self.days_buttons_group = QGroupBox("Days")  
        self.days_buttons_layout = QGridLayout()  
        self.days_buttons_layout.setContentsMargins(0,0,0,0)
        self.days_buttons_group.setContentsMargins(0,0,0,0)
        self.scroll_area_days = QScrollArea()  
        self.scroll_area_days.setWidgetResizable(True)  
        self.days_button_frame = QFrame()  
        self.days_buttons_layout = QGridLayout()  
        self.days_button_frame.setLayout(self.days_buttons_layout)  
        self.scroll_area_days.setWidget(self.days_button_frame)  
        self.days_buttons_group.setLayout(QVBoxLayout())  
        self.days_buttons_group.layout().addWidget(self.scroll_area_days)
        self.days_buttons_group.setLayout(self.days_buttons_layout)  
        self.days_layout = QHBoxLayout()  
        self.days_layout.addWidget(self.days_buttons_group, 80)  
        self.main_layout.addLayout(self.days_layout, 60)  
        self.days_layout.setContentsMargins(0,0,0,0)
        self.schedules_layout = QHBoxLayout()  
        self.schedules_buttons_group = QGroupBox("Schedules")  
        self.schedules_buttons_layout = QHBoxLayout()  
        self.scroll_area = QScrollArea()  
        self.scroll_area.setWidgetResizable(True)  
        self.button_frame = QFrame()  
        self.button_frame.setLayout(self.schedules_buttons_layout)  
        self.scroll_area.setWidget(self.button_frame)  
        self.schedules_buttons_group.setLayout(QVBoxLayout())  
        self.schedules_buttons_group.layout().addWidget(self.scroll_area)  
        self.schedules_layout.addWidget(self.schedules_buttons_group)  
        self.right_button_layout = QVBoxLayout()  
        self.add_button = QPushButton("Add Schedule")  
        self.delete_radio_button = QRadioButton("Delete Mode")  
        self.right_button_layout.addWidget(self.add_button)  
        self.right_button_layout.addWidget(self.delete_radio_button)  
        self.schedules_layout.addLayout(self.right_button_layout)  
        self.main_layout.addLayout(self.schedules_layout, 40)  
        self.expand_button = QPushButton("")   
        self.expand_button.setMinimumHeight(200)   
        self.expand_button.hide()
        self.layout.addLayout(self.main_layout, 80)   
        self.layout.addWidget(self.expand_button, 10)   
        self.expand_button.setStyleSheet("background-color: transparent; border-radius: 0px; image: url(C:/Users/r/Contacts/Desktop/9thgrade_project/assets/expand.png)")  
        self.add_button.clicked.connect(self.show_user_input_dialog)  
    def get_database(self,database):
        self.database=database
    def show_user_input_dialog(self):  
        dialog = UserInputDialog()
        if dialog.exec_() == QDialog.Accepted: 
            weight = dialog.weight_input.text()
            height = dialog.height_input.text()
            age = dialog.age_input.text()
            gender = dialog.gender
            ndays = dialog.days_input.text()
            activity_level=dialog.activity_level
            start_date = date.today()
            end_date = start_date + timedelta(days=int(ndays))
            data_id = current_user.logged_in_user.data_id
            counter=0
            number=current_user.logged_in_user.newest_schedule
            number=number+1
            current_user.logged_in_user.newest_schedule=number
            query2=QSqlQuery()
            query2.prepare("""INSERT INTO Data (id, weight, height, age, gender, days, start_date, end_date, data_days_state, number, name, data_days_calories, data_days_workout, bmi, ideal_weight, calories_per_day , carbohydrates, protein , fat)VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""")
            query2.addBindValue(data_id)
            query2.addBindValue(int(weight))
            query2.addBindValue(int(height))
            query2.addBindValue(int(age))
            query2.addBindValue(gender)
            query2.addBindValue(ndays)
            query2.addBindValue(str(start_date))
            query2.addBindValue(str(end_date))
            query2.addBindValue(cal.list_to_string(["none"]*int(ndays)))
            query2.addBindValue(number)
            Schedule_name = dialog.get_button_name() 
            query2.addBindValue(Schedule_name)
            query2.addBindValue(cal.list_to_string(["0"]*int(ndays)))
            query2.addBindValue(cal.list_to_string(["0"]*int(ndays)))
            bmi = cal.calculate_bmi(int(height),int(weight))
            ideal_weight = cal.calculate_ideal_weight(int(age),gender,int(height),int(bmi))
            calories_per_day=cal.calorys_needed_per_day(int(weight),int(ideal_weight),int(ndays),gender,int(height),int(age),activity_level)
            macronutrient_per_day = cal.calculate_macronutrient_needed_perday(int(weight),activity_level,int(age),gender)

            query2.addBindValue(bmi)
            query2.addBindValue(ideal_weight)
            query2.addBindValue(calories_per_day)
            query2.addBindValue(macronutrient_per_day.get("carbohydrates"))
            query2.addBindValue(macronutrient_per_day.get("protein"))
            query2.addBindValue(macronutrient_per_day.get("fat"))
            query2.exec_() 
            self.add_button_to_left_area(Schedule_name,number=number) 
    def add_button_to_left_area(self, Schedule_name,number):  
        new_push_button = ScheduleButton(Schedule_name,number=number)  
        new_push_button.clicked.connect(lambda: self.handle_button_click())  
        self.schedules_buttons_layout.addWidget(new_push_button)  
    
    
    def is_widget_in_layout(self, widget, layout):  
        for i in range(layout.count()):  
            item = layout.itemAt(i)  
            if item.widget() == widget:  
                return True  
        return False 
    
    def get_schedules(self):
        query1=QSqlQuery()
        query1.prepare("""SELECT * FROM Data WHERE id = ? """)
        query1.addBindValue(current_user.logged_in_user.data_id)
        query1.exec_()
        while query1.next():
            new_push_button = ScheduleButton(name=str(query1.value(10)),number=query1.value(9))  
            new_push_button.clicked.connect(lambda: self.handle_button_click())  
            if not self.is_widget_in_layout(new_push_button,self.schedules_buttons_layout):
                self.schedules_buttons_layout.addWidget(new_push_button)
            else:
                new_push_button.deleteLater()
  
    def handle_button_click(self):  
        sender = self.sender()  
        selected_schedule_num = sender.button_number  
        data_id = current_user.logged_in_user.data_id  
        if self.delete_radio_button.isChecked():  
            delete_query = QSqlQuery()  
            delete_query.prepare("""DELETE FROM Data WHERE id = ? and number = ?""")  
            delete_query.addBindValue(data_id)  
            delete_query.addBindValue(selected_schedule_num)  
            delete_query.exec_()  
            self.schedules_buttons_layout.removeWidget(sender)   
            sender.deleteLater()  
        else:
            current_user.logged_in_user.selected_schedule=selected_schedule_num
            while self.days_buttons_layout.count():  
                item = self.days_buttons_layout.takeAt(0)  
                widget = item.widget()   
                if widget is not None:  
                    widget.deleteLater()   
            query_days = QSqlQuery()  
            query_days.prepare("""SELECT * FROM Data WHERE id = ? and number = ?""")  
            query_days.addBindValue(data_id)  
            query_days.addBindValue(selected_schedule_num)  
            query_days.exec_()  
            if query_days.next():
                days = query_days.value(5)  
                start_date = query_days.value(6)  
                for i in range(int(days)):  
                    data_list = query_days.value(8)  
                    if isinstance(start_date, str): 
                        start_date = datetime.strptime(start_date, '%Y-%m-%d') 
                    data_list = cal.string_to_list(data_list)  
                    current_date = start_date + timedelta(days=i)  
                    state = data_list[i]
                    daybutton = DayButton(str(i+1), date=current_date, state=state)  
                    daybutton.setMinimumSize(50,50)
                    base_style = "font-size: 14px; font-weight: bold; color: White; border-radius: 0px;"  

                    if daybutton.date == date.today():  
                        today_style = "border-color: Blue; border-radius: 10px; border: 40px solid Blue;"  
                        daybutton.setStyleSheet(base_style + today_style)  
                    else:  
                        daybutton.setStyleSheet(base_style)  

                    if state == "done":  
                        daybutton.setStyleSheet(daybutton.styleSheet() +   
                                                "background-color: transparent; image: url(C:/Users/r/Contacts/Desktop/9thgrade_project/assets/done.png);")  
                    elif state == "none":  
                        daybutton.setStyleSheet(daybutton.styleSheet() +   
                                                "background-color: transparent; image: url(C:/Users/r/Contacts/Desktop/9thgrade_project/assets/none.png);")  
                    elif state == "undone":  
                        daybutton.setStyleSheet(daybutton.styleSheet() +   
                                                "background-color: transparent; image: url(C:/Users/r/Contacts/Desktop/9thgrade_project/assets/undone.png);")  
                    elif state == "perfect":  
                        daybutton.setStyleSheet(daybutton.styleSheet() +   
                                                "background-color: transparent; image: url(C:/Users/r/Contacts/Desktop/9thgrade_project/assets/perfect.png);")  
                    x=i%7
                    y=(i-i%7)/7
                    self.days_buttons_layout.addWidget(daybutton,int(y),int(x)) 
                self.expand_button.show()
    def load_schedule_days(self):
        selected_schedule_num = current_user.logged_in_user.selected_schedule
        data_id = current_user.logged_in_user.data_id
        while self.days_buttons_layout.count():  
            item = self.days_buttons_layout.takeAt(0)  
            widget = item.widget()   
            if widget is not None:  
                widget.deleteLater()   
        query_days = QSqlQuery()  
        query_days.prepare("""SELECT * FROM Data WHERE id = ? and number = ?""")  
        query_days.addBindValue(data_id)  
        query_days.addBindValue(selected_schedule_num)  
        query_days.exec_()  
        if query_days.next():
            days = query_days.value(5)  
            start_date = query_days.value(6)  
            for i in range(int(days)):  
                data_list = query_days.value(8)  
                if isinstance(start_date, str): 
                    start_date = datetime.strptime(start_date, '%Y-%m-%d') 
                data_list = cal.string_to_list(data_list)  
                current_date = start_date + timedelta(days=i)  
                state = data_list[i]
                daybutton = DayButton(str(i+1), date=current_date, state=state)  
                daybutton.setMinimumSize(50,50)
                base_style = "font-size: 14px; font-weight: bold; color: White; border-radius: 0px;"  

                if daybutton.date == date.today():  
                    today_style = "border-color: Blue; border-radius: 10px; border: 40px solid Blue;"  
                    daybutton.setStyleSheet(base_style + today_style)  
                else:  
                    daybutton.setStyleSheet(base_style)  

                if state == "done":  
                    daybutton.setStyleSheet(daybutton.styleSheet() +   
                                            "background-color: transparent; image: url(C:/Users/r/Contacts/Desktop/9thgrade_project/assets/done.png);")  
                elif state == "none":  
                    daybutton.setStyleSheet(daybutton.styleSheet() +   
                                            "background-color: transparent; image: url(C:/Users/r/Contacts/Desktop/9thgrade_project/assets/none.png);")  
                elif state == "undone":  
                    daybutton.setStyleSheet(daybutton.styleSheet() +   
                                            "background-color: transparent; image: url(C:/Users/r/Contacts/Desktop/9thgrade_project/assets/undone.png);")  
                elif state == "perfect":  
                    daybutton.setStyleSheet(daybutton.styleSheet() +   
                                            "background-color: transparent; image: url(C:/Users/r/Contacts/Desktop/9thgrade_project/assets/perfect.png);")  
                x=i%7
                y=(i-i%7)/7
                self.days_buttons_layout.addWidget(daybutton,int(y),int(x)) 
            self.expand_button.show()
    def connect_buttons(self,tabs):
        pass
