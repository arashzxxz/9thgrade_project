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
            query1=QSqlQuery()
            query1.prepare("""SELECT * FROM Data WHERE id = ? """)
            query1.exec_()
            h=hash.new("SHA256")
            h.update(data_id.encode())
            data_id=h.hexdigest()
            query1.addBindValue(data_id)
            while query1.next():
                counter = counter+1
            counter = counter+1
            current_user.logged_in_user.newest_schedule=counter
            query2=QSqlQuery()
            query2.prepare("""INSERT INTO Data (id, weight, height, age, gender, days, start_date, end_date, data, number)VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?)""")
            query2.addBindValue(data_id)
            query2.addBindValue(weight)
            query2.addBindValue(height)
            query2.addBindValue(age)
            query2.addBindValue(gender)
            query2.addBindValue(ndays)
            query2.addBindValue(start_date)
            query2.addBindValue(end_date)
            query2.addBindValue("?")
            query2.addBindValue(counter)
            query2.exec_() 
            Schedule_name = dialog.get_button_name()  
            self.add_button_to_left_area(Schedule_name)  

    def add_button_to_left_area(self, Schedule_name):  
        new_push_button = QPushButton(Schedule_name)  
        new_push_button.clicked.connect(lambda: self.handle_button_click(new_push_button))  
        self.schedules_buttons_layout.addWidget(new_push_button)  

    def handle_button_click(self, button):  
        if self.delete_radio_button.isChecked():  
            self.schedules_buttons_layout.removeWidget(button) 
            button.deleteLater()

    def connect_buttons(self,tabs):
        self.expand_button.clicked.connect(lambda : tabs.setCurrentIndex(0))
