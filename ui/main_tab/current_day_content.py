import sys  
from PyQt5.QtWidgets import QApplication,QColorDialog,QMainWindow,QScrollArea,QStyleFactory,QStackedWidget,QTreeView,QDateEdit,QTableWidgetItem,QMessageBox,QTabWidget, QWidget,QFileDialog, QLabel,QListWidget ,QComboBox,QPushButton ,QVBoxLayout,QTableWidget,QVBoxLayout,QHBoxLayout,QGridLayout,QCheckBox,QRadioButton,QButtonGroup,QLineEdit
from PyQt5.QtCore import Qt, QDate  
import main
from ui.main_tab import calendar_widget,current_day_content
from assets.assests import get_assets_working_dir
class Current_day_exercise_widget(QWidget):  
    def __init__(self):  
        super().__init__()  
        # create the layouts
        self.main_layout=QHBoxLayout()
        #-------------------

        #add the widgets
        self.expand_button=QPushButton("",self)
        self.exercise_status_text=QLabel("20 minutes of exersice needed",self)
        self.exercise_status_icon=QLabel("",self)
        self.workout_time_entry=QLineEdit(self)
        self.expand_button.setStyleSheet("background-color: transparent;border-radius: 0px ;image: url("+get_assets_working_dir()+"expand.png)")
        #---------------

        #set the layouts contents
        self.main_layout.addWidget(self.exercise_status_icon,20)
        self.main_layout.addWidget(self.exercise_status_text,30)
        self.main_layout.addWidget(self.workout_time_entry,30)
        self.main_layout.addWidget(self.expand_button,20)
        self.setLayout(self.main_layout)
        #--------------

class Current_day_food_widget(QWidget):  
    def __init__(self):  
        super().__init__()  
        # create the layouts
        self.main_layout=QHBoxLayout()
        self.needed_calories_text_layout=QHBoxLayout()
        self.eaten_calories_text_layout=QHBoxLayout()
        self.content_layout=QVBoxLayout()
        #-------------------

        #add the widgets
        self.needed_calories_text=QLabel("Needed calories :",self)
        self.needed_calories_text2=QLabel("740",self)
        self.needed_calories_text2.setAlignment(Qt.AlignRight | Qt.AlignVCenter)
        self.eaten_calories_text=QLabel("Eaten calories   :",self)
        self.eaten_calories_entry=QLineEdit(self)
        self.expand_button=QPushButton("",self)
        self.expand_button.setStyleSheet("background-color: transparent;border-radius: 0px ;image: url("+get_assets_working_dir()+"expand.png)")
        #---------------

        #set the layouts contents
        self.needed_calories_text_layout.addWidget(self.needed_calories_text)
        self.needed_calories_text_layout.addWidget(self.needed_calories_text2)
        self.eaten_calories_text_layout.addWidget(self.eaten_calories_text,80)
        self.eaten_calories_text_layout.addWidget(self.eaten_calories_entry,20)
        self.content_layout.addLayout(self.needed_calories_text_layout)
        self.content_layout.addLayout(self.eaten_calories_text_layout)
        self.main_layout.addLayout(self.content_layout,60)
        self.main_layout.addWidget(self.expand_button,20)
        self.setLayout(self.main_layout)
        #--------------