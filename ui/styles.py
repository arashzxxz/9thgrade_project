from ui import Menu, Settings_Tab,styles
from PyQt5.QtCore import Qt,QTime,QTimer,QDate,QSize
from PyQt5.QtWidgets import QApplication,QMainWindow,QTreeView,QDateEdit,QTableWidgetItem,QMessageBox,QTabWidget, QWidget,QFileDialog, QLabel,QListWidget ,QComboBox,QPushButton ,QVBoxLayout,QTableWidget,QVBoxLayout,QHBoxLayout,QGridLayout,QCheckBox,QRadioButton,QButtonGroup,QLineEdit
from PyQt5.QtGui import QIcon,QFont,QPixmap,QFontDatabase
class style_sheets(QWidget):
    settings_customaization_tab="""
    QPushButton#back_button{
        padding: 25px 25px 25px 25px;
        background: transparent;
    }
    """
    settings_style="""
    QLabel#separator1{
        border : solid black;
        border-width : 5px 0px 0px 0px;
    }
    QLabel#separator2{
        border : solid black;
        border-width : 5px 0px 0px 0px;
    }
    QLabel#separator3{
        border : solid black;
        border-width : 5px 0px 0px 0px;
    }
    QLabel#header1{
        font:30px;
        font-family: Arial;
    }
    QLabel#header2{
        font:30px;
        font-family: Arial;
    }
    QLabel#header3{
        font:30px;
        font-family: Arial;
    }
    """