import sys  
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout,  QPushButton, QLabel, QScrollArea  
from PyQt5.QtCore import Qt, QDate  
import main
from ui.main_tab import main_widget,current_day_content
    

class Calendar_widget(QWidget):  
    def __init__(self):  
        super().__init__()  
        self.main_layout=QVBoxLayout()


        # Create a scroll area for the buttons  
        self.scroll_area = QScrollArea(self)  
        self.scroll_area.setWidgetResizable(True)  
        #-------------------------------------

        # Create a widget to hold the buttons  
        self.button_widget = QWidget()  
        self.button_layout = QVBoxLayout(self.button_widget) 
        #------------------------------------ 

        # Create and add buttons  
        self.create_calendar_buttons()  
        self.scroll_area.setWidget(self.button_widget)  
        self.main_layout.addWidget(self.scroll_area)  
        #----------------------------

        #set the layout
        self.setLayout(self.main_layout)
        #--------------

    def create_calendar_buttons(self):  
        # Get the current months date  
        current_date = QDate.currentDate()  
        year = current_date.year()  
        month = current_date.month()  
        num_days = current_date.daysInMonth() 
        #----------------------------

        # Create buttons for each day of the month  
        for day in range(1, num_days + 1):  
            button = QPushButton(str(day))  
            button.setMinimumSize(50, 50)  
            button.clicked.connect(lambda checked, d=day: self.date_selected(year, month, d))  
            self.button_layout.addWidget(button) 
        #----------------------------------------- 

    #show the selected date
    def date_selected(self, year, month, day):  
        #(f"Selected Date: {year}-{month:02d}-{day:02d}")  
        pass
    #----------------------
