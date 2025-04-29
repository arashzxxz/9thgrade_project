import sys  
from PyQt5.QtWidgets import QApplication, QMainWindow, QWidget, QVBoxLayout,  QPushButton, QLabel, QScrollArea  
from PyQt5.QtCore import Qt, QDate 
from PyQt5.QtSql import QSqlDatabase,QSqlQuery
import main
from calculations.calculations import string_to_list,list_to_string
from datetime import date,timedelta,datetime
from data.day_button_handle import set_state
from ui.main_tab import main_widget,current_day_content
from users import current_user
from assets.assests import get_assets_working_dir
class DayButton(QPushButton):
    def __init__(self,name,date,state):  
        super().__init__(name)  
        self.date=date
        self.state=state


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
        self.scroll_area.setWidget(self.button_widget)  
        self.main_layout.addWidget(self.scroll_area)  
        #----------------------------

        #set the layout
        self.setLayout(self.main_layout)
        #--------------
    def get_data_base(self,data_base):
        self.database=data_base
    def get_main_widget(self,main_widget):
        self.main_widget=main_widget
    def create_calendar_buttons(self):  
        # Get the current months date 
        while self.button_layout.count():  
            item = self.button_layout.takeAt(0)  
            widget = item.widget()   
            if widget is not None:  
                widget.deleteLater()   
        query_days = QSqlQuery()  
        query_days.prepare("""SELECT * FROM Data WHERE id = ? and number = ?""")  
        query_days.addBindValue(current_user.logged_in_user.data_id)  
        query_days.addBindValue(current_user.logged_in_user.selected_schedule)  
        query_days.exec_()  
        if query_days.next():
            num_days = query_days.value(5) 
            start_date = query_days.value(6)  
            for i in range(int(num_days)):  
                data_list = query_days.value(8)  
                if isinstance(start_date, str): 
                    start_date = datetime.strptime(start_date, '%Y-%m-%d') 
                data_list = string_to_list(data_list)  
                current_date = start_date + timedelta(days=i)  
                state = data_list[i]  
                daybutton = DayButton(str(i+1), date=current_date, state=state)  
                daybutton.clicked.connect(lambda : set_state(self.database,self.main_widget,state))
                daybutton.setMinimumSize(50,50)
                base_style = "font-size: 14px; font-weight: bold; color: White; border-radius: 0px;"  

                if daybutton.date == date.today():  
                    today_style = "border-color: Blue; border-radius: 10px; border: 40px solid Blue;"  
                    daybutton.setStyleSheet(base_style + today_style)  
                else:  
                    daybutton.setStyleSheet(base_style)  

                if state == "done":  
                    daybutton.setStyleSheet(daybutton.styleSheet() +   
                                            "background-color: transparent; image: url("+get_assets_working_dir()+"done.png);")  
                elif state == "none":  
                    daybutton.setStyleSheet(daybutton.styleSheet() +   
                                            "background-color: transparent; image: url("+get_assets_working_dir()+"none.png);")  
                elif state == "undone":  
                    daybutton.setStyleSheet(daybutton.styleSheet() +   
                                            "background-color: transparent; image: url("+get_assets_working_dir()+"undone.png);")  
                elif state == "perfect":  
                    daybutton.setStyleSheet(daybutton.styleSheet() +   
                                            "background-color: transparent; image: url("+get_assets_working_dir()+"perfect.png);")  
                self.button_layout.addWidget(daybutton) 
        #----------------------------------------- 

