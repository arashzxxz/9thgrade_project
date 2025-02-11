import sys 
import datetime 
from PyQt5.QtWidgets import QApplication,QColorDialog,QMainWindow,QScrollArea,QStyleFactory,QStackedWidget,QTreeView,QDateEdit,QTableWidgetItem,QMessageBox,QTabWidget, QWidget,QFileDialog, QLabel,QListWidget ,QComboBox,QPushButton ,QVBoxLayout,QTableWidget,QVBoxLayout,QHBoxLayout,QGridLayout,QCheckBox,QRadioButton,QButtonGroup,QLineEdit
from PyQt5.QtCore import Qt, QDate  
import main
from ui.main_tab import calendar_widget,current_day_content
    

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
        self.current_day_content1=current_day_content.Current_day_food_widget()
        self.current_day_content2=current_day_content.Current_day_exercise_widget()
        self.date=QLabel("Dec 4, 2024",self)
        self.date.setStyleSheet("font-size: 20px")
        self.date.setAlignment(Qt.AlignLeft | Qt.AlignVCenter)
        self.date.setText(str(datetime.date.today()))
        self.backbutton=QPushButton("",self)
        self.backbutton.setStyleSheet("background-color: transparent; border-radius: 0px; image: url(C:/Users/r/Contacts/Desktop/9thgrade_project/assets/back.png)")
        self.top_buttons_layout.addWidget(self.backbutton,1)
        self.top_buttons_layout.addWidget(self.date,3)
        self.current_day_content.addLayout(self.top_buttons_layout,10)
        self.current_day_content.addWidget(self.current_day_content1,60)
        self.current_day_content.addWidget(self.current_day_content2,30)
        self.main_layout.addWidget(self.calendar_widget,30)
        self.main_layout.addLayout(self.current_day_content,70)
        #---------------

        #set the layout
        self.setLayout(self.main_layout)
        #--------------

    #connect all the buttons
    def connect_buttons(self,tabs):
        self.current_day_content2.expand_button.clicked.connect(lambda : tabs.setCurrentIndex(5))
        self.current_day_content1.expand_button.clicked.connect(lambda : tabs.setCurrentIndex(8))
        self.backbutton.clicked.connect(lambda : tabs.setCurrentIndex(7))
    #-----------------------
        
