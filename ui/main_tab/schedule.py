import sys  
from PyQt5.QtWidgets import QApplication,QColorDialog,QMainWindow,QScrollArea,QStyleFactory,QStackedWidget,QTreeView,QDateEdit,QTableWidgetItem,QMessageBox,QTabWidget, QWidget,QFileDialog, QLabel,QListWidget ,QComboBox,QPushButton ,QVBoxLayout,QTableWidget,QVBoxLayout,QHBoxLayout,QGridLayout,QCheckBox,QRadioButton,QButtonGroup,QLineEdit
from PyQt5.QtCore import Qt, QDate  
import main
from ui.main_tab import calendar_widget,current_day_content
    

class scheduls_tab(QWidget):  
    def __init__(self):  
        super().__init__()  
        # create the widgets
        self.current_day_content=QVBoxLayout()
        self.main_layout=QHBoxLayout()
        #-------------------
        
