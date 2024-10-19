
import sys
import random
import requests
import os
from ui import Menu, Settings_Tab,styles
from PyQt5.QtSql import QSqlDatabase,QSqlQuery
from PyQt5.QtCore import Qt,QTime,QTimer,QDate,QSize
from PyQt5.QtWidgets import QApplication,QColorDialog,QMainWindow,QScrollArea,QStackedWidget,QTreeView,QDateEdit,QTableWidgetItem,QMessageBox,QTabWidget, QWidget,QFileDialog, QLabel,QListWidget ,QComboBox,QPushButton ,QVBoxLayout,QTableWidget,QVBoxLayout,QHBoxLayout,QGridLayout,QCheckBox,QRadioButton,QButtonGroup,QLineEdit
from PyQt5.QtGui import QIcon,QFont,QPixmap,QFontDatabase,QStandardItemModel,QStandardItem
class mainw(QMainWindow):
    def __init__(self):
        #create main window
        super(mainw,self).__init__()
        self.setWindowTitle('app')
        self.Width = 1000
        self.height = int(0.618 * self.Width)
        self.resize(self.Width, self.height)
        #------------------


        #create tabs and menus and connecting buttons
        self.initui()
        self.connect_all_buttons()
        #--------------------------------------------


    def connect_all_buttons(self):
        self.main_menu.connect_buttons(self.tabs)


    def initui(self):
        #create all of the main tabs
        self.content_tab1=self.createtab1()
        self.content_tab2=self.createtab2()
        self.settings_tab=Settings_Tab.setting_tab()
        self.settings_tab.setObjectName("settings_tab")
        self.settings_customization_tab=Settings_Tab.setting_customization_tab()
        #---------------------------

        #connect all of the tabs
        self.tabs=QTabWidget()
        self.tabs.addTab(self.content_tab1,"")
        self.tabs.addTab(self.content_tab2,"")
        self.tabs.addTab(self.settings_tab,"")
        self.tabs.addTab(self.settings_customization_tab,"")
        self.tabs.setCurrentIndex(3)
        self.tabs.setStyleSheet('''QTabBar::tab{width: 0;height: 0; margin: 0; padding: 0; border: none;}''')
        #-----------------------


        #create main layout and menu
        self.main_layout=QHBoxLayout(self)
        self.main_menu=Menu.menu()
        self.main_layout.addWidget(self.main_menu,0)
        self.main_layout.addWidget(self.tabs,1)
        self.main_layout.setContentsMargins(0,0,0,0)
        self.main_widget=QWidget()
        self.main_widget.setLayout(self.main_layout)
        self.setCentralWidget(None)
        self.setCentralWidget(self.main_widget)
        #---------------------------

        #style all of the app
        self.set_styles()
        #-------------------
    

    #test tab
    def createtab1(self):
        vb1=QVBoxLayout()
        vb1.addWidget(QPushButton("1",self))
        gui=QWidget()
        gui.setLayout(vb1)
        return gui
    #-------

    #test tab
    def createtab2(self):
        vb1=QVBoxLayout()
        vb1.addWidget(QPushButton("2",self))
        gui=QWidget()
        gui.setLayout(vb1)
        return gui
    #--------


    def set_styles(self):
        self.settings_tab.setStyleSheet(styles.style_sheets.settings_style)
        self.settings_customization_tab.setStyleSheet(styles.style_sheets.settings_customaization_tab)


def main():
    app=QApplication(sys.argv)
    window=mainw()
    window.show()
    sys.exit(app.exec_())
if __name__ == "__main__":
    main()