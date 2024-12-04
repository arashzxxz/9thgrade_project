import sys  
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
        #-------------------

        #add the widgets
        self.calendar_widget=calendar_widget.Calendar_widget()
        self.current_day_content=current_day_content.Current_day_content_widget()
        self.main_layout.addWidget(self.calendar_widget,30)
        self.main_layout.addWidget(self.current_day_content,70)
        #---------------

        #set the layout
        self.setLayout(self.main_layout)
        #--------------
        
