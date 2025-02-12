import sys  
import hashlib as hash
import re
from datetime import date,timedelta
from PyQt5.QtSql import QSqlDatabase,QSqlQuery
from users import current_user
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget,  
                             QVBoxLayout, QHBoxLayout, QRadioButton,  
                             QPushButton, QGroupBox, QScrollArea,  
                             QFrame, QDialog, QLabel, QLineEdit)  

def string_to_list(string, separator=', '):  
    return string.split(separator) 
def list_to_string(list, separator=', '):  
    return separator.join(map(str, list)) 

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
        self.gender_input = QLineEdit(self)  
        self.gender_input.setPlaceholderText("Gender")  
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
        self.layout.addWidget(self.gender_input)  
        self.layout.addWidget(QLabel("Number of days:"))
        self.layout.addWidget(self.days_input)
        self.layout.addWidget(self.submit_button)  
        self.setLayout(self.layout)  
        self.Schedule_name = None  

    def submit_data(self):  
        name = self.name_input.text()  
        self.Schedule_name = name   
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
        self.days_buttons_layout = QVBoxLayout()  
        self.days_buttons_group.setLayout(self.days_buttons_layout)  
        self.days_layout = QHBoxLayout()  
        self.days_layout.addWidget(self.days_buttons_group, 80)  
        self.main_layout.addLayout(self.days_layout, 60)  
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
        self.add_button = QPushButton("Add Button")  
        self.delete_radio_button = QRadioButton("Delete Button")  
        self.right_button_layout.addWidget(self.add_button)  
        self.right_button_layout.addWidget(self.delete_radio_button)  
        self.schedules_layout.addLayout(self.right_button_layout)  
        self.main_layout.addLayout(self.schedules_layout, 40)  
        self.expand_button = QPushButton("")   
        self.expand_button.setMinimumHeight(200)   
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
            gender = dialog.gender_input.text()
            ndays = dialog.days_input.text()
            start_date = date.today()
            end_date = start_date + timedelta(days=int(ndays))
            data_id = current_user.logged_in_user.data_id
            counter=0
            number=current_user.logged_in_user.newest_schedule
            number=number+1
            current_user.logged_in_user.newest_schedule=number
            query2=QSqlQuery()
            query2.prepare("""INSERT INTO Data (id, weight, height, age, gender, days, start_date, end_date, data, number)VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""")
            query2.addBindValue(data_id)
            query2.addBindValue(int(weight))
            query2.addBindValue(int(height))
            query2.addBindValue(int(age))
            query2.addBindValue(gender)
            query2.addBindValue(ndays)
            query2.addBindValue(str(start_date))
            query2.addBindValue(str(end_date))
            query2.addBindValue(list_to_string(["undone"]*int(ndays)))
            query2.addBindValue(number)
            Schedule_name = dialog.get_button_name() 
            query2.addBindValue(Schedule_name)
            query2.exec_() 
            self.add_button_to_left_area(Schedule_name,number=number) 
    def add_button_to_left_area(self, Schedule_name,number):  
        new_push_button = ScheduleButton(Schedule_name,number=number)  
        new_push_button.clicked.connect(lambda: self.handle_button_click(new_push_button))  
        self.schedules_buttons_layout.addWidget(new_push_button)  
    
    def get_schedules(self):
        query1=QSqlQuery()
        query1.prepare("""SELECT * FROM Data WHERE id = ? """)
        query1.addBindValue(current_user.logged_in_user.data_id)
        query1.exec_()
        if query1.next():
            new_push_button = ScheduleButton(name=str(query1.value(10)),number=query1.value(9))  
            new_push_button.clicked.connect(lambda: self.handle_button_click(new_push_button))  
            self.schedules_buttons_layout.addWidget(new_push_button)  
    def handle_button_click(self, button):  
        if self.delete_radio_button.isChecked():  
            self.schedules_buttons_layout.removeWidget(button) 
            button.deleteLater()
        else : 
            query_days=QSqlQuery()
            sender = self.sender()
            selected_schedule_num=sender.button_number
            print(selected_schedule_num)
            data_id = current_user.logged_in_user.data_id
            h=hash.new("SHA256")
            h.update(str(data_id).encode())
            data_id=h.hexdigest()
            query_days.prepare("""SELECT * FROM Data WHERE id = ? and number = ?""")
            query_days.addBindValue(data_id)
            query_days.addBindValue(selected_schedule_num)
            query_days.exec_()
            days=query_days.value(5)
            print(days)
            start_date=query_days.value(6)
            for i in range(int(days)):
                number=selected_schedule_num
                data_list=query_days.value(8)
                data_list=string_to_list(data_list)
                current_date = start_date + timedelta(days=i)
                state=data_list[i]
                button=DayButton(str(i),date=current_date,state=state)
                if state=="done":
                            button.setStyleSheet("background-color: transparent; border-radius: 0px; image: url(C:/Users/r/Contacts/Desktop/9thgrade_project/assets/done.png)")
                if state=="none":
                            button.setStyleSheet("background-color: transparent; border-radius: 0px; image: url(C:/Users/r/Contacts/Desktop/9thgrade_project/assets/none.png)")
                if state=="undone":
                            button.setStyleSheet("background-color: transparent; border-radius: 0px; image: url(C:/Users/r/Contacts/Desktop/9thgrade_project/assets/undone.png)")
                if state=="perfect":
                            button.setStyleSheet("background-color: transparent; border-radius: 0px; image: url(C:/Users/r/Contacts/Desktop/9thgrade_project/assets/perfect.png)")
                self.days_layout.addWidget(button)
            # select every day in the schedule

    def connect_buttons(self,tabs):
        self.expand_button.clicked.connect(lambda : tabs.setCurrentIndex(0))
