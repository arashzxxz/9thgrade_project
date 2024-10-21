from ui import Menu, Settings_Tab,styles
from PyQt5.QtCore import Qt,QTime,QTimer,QDate,QSize
from PyQt5.QtWidgets import QApplication,QMainWindow,QTreeView,QDateEdit,QTableWidgetItem,QMessageBox,QTabWidget, QWidget,QFileDialog, QLabel,QListWidget ,QComboBox,QPushButton ,QVBoxLayout,QTableWidget,QVBoxLayout,QHBoxLayout,QGridLayout,QCheckBox,QRadioButton,QButtonGroup,QLineEdit
from PyQt5.QtGui import QIcon,QFont,QPixmap,QFontDatabase
class style_sheets(QWidget):
    backgroundc="#2f3030"
    borderc="Green"
    selected_tabc="rgba(24, 99, 22, 255)"
    widgetsc="rgba(24, 99, 22, 100)"
    widgets_hoverc="rgba(24, 99, 22, 150)"
    menu_backgroundc="Black"
    menu_widgetsc="Blue"
    required_settings_customaization_tab="""
    QPushButton#back_button{
        padding: 25px 25px 25px 25px;
        background: transparent;
    }
    """
    requierd_settings_style="""
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
    main_style="""
    background-color: """+backgroundc+""";
    QPushButton{
        background-color: """+widgetsc+""";
    }
    QPushButton:hover{
        background-color: """+widgets_hoverc+""";
    }
    """
    menu_style="""
        QRadioButton#menub::indicator::unchecked{
                           background-color: transparent;
                           border-radius: 0px ;
                           image: url(C:/Users/r/Contacts/Desktop/9thgrade_project/assets/menu.png)
                           
        }
        QRadioButton#menub::indicator::checked{
                           background-color: """+selected_tabc+""";
                           border-radius: 0px ;
                           image: url(C:/Users/r/Contacts/Desktop/9thgrade_project/assets/menu.png)
                           
        }
        QRadioButton#settingb::indicator::unchecked{
                           background-color: transparent;
                           border-radius: 0px ;
                           image: url(C:/Users/r/Contacts/Desktop/9thgrade_project/assets/settings.png)
                           
        }
        QRadioButton#settingb::indicator::checked{
                           background-color: """+selected_tabc+""";
                           border-radius: 0px ;
                           image: url(C:/Users/r/Contacts/Desktop/9thgrade_project/assets/settings.png)
                           
        }
        QRadioButton#homeb::indicator::unchecked{
                           background-color: transparent;
                           border-radius: 0px ;
                           image: url(C:/Users/r/Contacts/Desktop/9thgrade_project/assets/home.png)
                           
        }
        QRadioButton#homeb::indicator::checked{
                           background-color: """+selected_tabc+""";
                           border-radius: 0px ;
                           image: url(C:/Users/r/Contacts/Desktop/9thgrade_project/assets/home.png)
                           
        }
        QRadioButton#statusb::indicator::unchecked{
                           background-color: transparent;
                           border-radius: 0px ;
                           image: url(C:/Users/r/Contacts/Desktop/9thgrade_project/assets/status.png)
                           
        }
        QRadioButton#statusb::indicator::checked{
                           background-color: """+selected_tabc+""";
                           border-radius: 0px ;
                           image: url(C:/Users/r/Contacts/Desktop/9thgrade_project/assets/status.png)
                           
        }
    QRadioButton{
    }
    QRadioButton:hover{
        background-color: """+widgets_hoverc+"""
    }

    """