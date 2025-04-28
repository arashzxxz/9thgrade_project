from ui import Menu, Settings_Tab,styles
from PyQt5.QtCore import Qt,QTime,QTimer,QDate,QSize
from PyQt5.QtWidgets import QApplication,QMainWindow,QTreeView,QDateEdit,QTableWidgetItem,QMessageBox,QTabWidget, QWidget,QFileDialog, QLabel,QListWidget ,QComboBox,QPushButton ,QVBoxLayout,QTableWidget,QVBoxLayout,QHBoxLayout,QGridLayout,QCheckBox,QRadioButton,QButtonGroup,QLineEdit
from PyQt5.QtGui import QIcon,QFont,QPixmap,QFontDatabase
from assets.assests import get_assets_working_dir
class style_sheets(QWidget):
    wd = get_assets_working_dir()
    backgroundc="#2f3030"
    borderc="Green"
    selected_tabc="rgba(24, 99, 22, 255)"
    widgetsc="rgba(24, 99, 22, 100)"
    widgets_hoverc="rgba(24, 99, 22, 150)"
    menu_backgroundc="Black"
    menu_widgetsc="Blue"
    menu_style="""
        QRadioButton#menub::indicator::unchecked{
                           background-color: transparent;
                           border-radius: 0px;
                           image: url(C:/Users/r/Contacts/Desktop/9thgrade_project/assets/menu.png);
                           
        }
        QRadioButton#menub::indicator::checked{
                           background-color: """+selected_tabc+""";
                           border-radius: 0px;
                           image: url(C:/Users/r/Contacts/Desktop/9thgrade_project/assets/menu.png);
                           
        }
        QRadioButton#settingb::indicator::unchecked{
                           background-color: transparent;
                           border-radius: 0px ;
                           image: url(C:/Users/r/Contacts/Desktop/9thgrade_project/assets/settings.png);
                           
        }
        QRadioButton#settingb::indicator::checked{
                           background-color: """+selected_tabc+""";
                           border-radius: 0px ;
                           image: url(C:/Users/r/Contacts/Desktop/9thgrade_project/assets/settings.png);
                           
        }
        QRadioButton#homeb::indicator::unchecked{
                           background-color: transparent;
                           border-radius: 0px ;
                           image: url(C:/Users/r/Contacts/Desktop/9thgrade_project/assets/home.png);
                           
        }
        QRadioButton#homeb::indicator::checked{
                           background-color: """+selected_tabc+""";
                           border-radius: 0px ;
                           image: url(C:/Users/r/Contacts/Desktop/9thgrade_project/assets/home.png);
                           
        }
        QRadioButton#statusb::indicator::unchecked{
                           background-color: transparent;
                           border-radius: 0px ;
                           image: url(C:/Users/r/Contacts/Desktop/9thgrade_project/assets/status.png);
                           
        }
        QRadioButton#statusb::indicator::checked{
                           background-color: """+selected_tabc+""";
                           border-radius: 0px ;
                           image: url(C:/Users/r/Contacts/Desktop/9thgrade_project/assets/status.png);
                           
        }
        QRadioButton#usersb::indicator::unchecked{
                           background-color: transparent;
                           border-radius: 0px ;
                           image: url(C:/Users/r/Contacts/Desktop/9thgrade_project/assets/users.png);
                           
        }
        QRadioButton#usersb::indicator::checked{
                           background-color: """+selected_tabc+""";
                           border-radius: 0px ;
                           image: url(C:/Users/r/Contacts/Desktop/9thgrade_project/assets/users.png);
                           
        }
        QRadioButton#streakb::indicator::unchecked{
                           background-color: transparent;
                           border-radius: 0px ;
                           image: url(C:/Users/r/Contacts/Desktop/9thgrade_project/assets/streak_undone.png);
                           
        }
        QRadioButton#streakb::indicator::checked{
                           background-color: transparent;
                           border-radius: 0px ;
                           image: url(C:/Users/r/Contacts/Desktop/9thgrade_project/assets/streak_undone.png);
                           
        }
    QRadioButton:hover{
        background-color: #014d02;
    }

    """