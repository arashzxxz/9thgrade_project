
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QHBoxLayout,QStackedWidget,  QLabel, QListWidget, QMessageBox,QPushButton
from ui.main_tab import timer,exercise_suggestion

class Exercise_tab(QWidget):  
    def __init__(self):  
        super().__init__()  

        #create the widgets 
        self.choose_timer_tab=QPushButton("Timer",self)
        self.choose_Suggestions_tab=QPushButton("Suggestions",self)
        self.timer_widget=timer.Timer()
        self.suggestions_widget=exercise_suggestion.Exercise_suggestions()
        self.tabs=QStackedWidget()
        self.tabs.addWidget(self.timer_widget)
        self.tabs.addWidget(self.suggestions_widget)
        #------------------

        #set the layouts
        self.main_layout=QVBoxLayout()
        self.button_layout=QHBoxLayout()
        self.button_layout.addWidget(self.choose_timer_tab)
        self.button_layout.addWidget(self.choose_Suggestions_tab)
        self.button_layout.setContentsMargins(100,10,100,10)
        self.main_layout.addLayout(self.button_layout)
        self.main_layout.addWidget(self.tabs)
        self.setLayout(self.main_layout)
        #------------------

    #connect all the buttons 
    def connect_buttons(self):
        self.choose_timer_tab.clicked.connect(lambda : self.tabs.setCurrentIndex(0))
        self.choose_Suggestions_tab.clicked.connect(lambda : self.tabs.setCurrentIndex(1))

