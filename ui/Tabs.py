
from ui import styles
from PyQt5.QtSql import QSqlDatabase,QSqlQuery
from PyQt5.QtCore import Qt,QTime,QTimer,QDate,QSize
from PyQt5.QtWidgets import QApplication,QMainWindow,QTreeView,QScrollArea,QStackedWidget,QDateEdit,QTableWidgetItem,QMessageBox,QTabWidget, QWidget,QFileDialog, QLabel,QListWidget ,QComboBox,QPushButton ,QVBoxLayout,QTableWidget,QVBoxLayout,QHBoxLayout,QGridLayout,QCheckBox,QRadioButton,QButtonGroup,QLineEdit
from PyQt5.QtGui import QIcon,QFont,QPixmap,QFontDatabase


class setting_tab(QWidget):
    def __init__(self):
        super().__init__()
        #create texts and headers
        self.customization_header=QLabel("Customization",self)
        self.section_seperator1=QLabel("",self)
        self.notification_header=QLabel("Notification",self)
        self.section_seperator2=QLabel("",self)
        self.data_header=QLabel("Data",self)
        self.section_seperator3=QLabel("",self)
        self.data_header.setObjectName("header3")
        self.notification_header.setObjectName("header2")
        self.customization_header.setObjectName("header1")
        self.section_seperator3.setObjectName("separator3")
        self.section_seperator2.setObjectName("separator2")
        self.section_seperator1.setObjectName("separator1")
        #-----------------------



        #create layout
        self.sections_layout=QVBoxLayout(self)
        self.settings_sections_tab=QWidget()
        self.customization_content=self.settings_customization()
        self.notification_content=self.settings_notification()
        self.data_content=self.settings_data()
        self.sections_layout.addWidget(self.customization_header,20)
        self.sections_layout.addWidget(self.section_seperator1,10)
        self.sections_layout.addWidget(self.customization_content)
        self.sections_layout.addWidget(self.notification_header,20)
        self.sections_layout.addWidget(self.section_seperator2,10)
        self.sections_layout.addWidget(self.notification_content)
        self.sections_layout.addWidget(self.data_header,20)
        self.sections_layout.addWidget(self.section_seperator3,10)
        self.sections_layout.addWidget(self.data_content)
        self.settings_sections_tab.setLayout(self.sections_layout)
        self.settings_main_tabs=QTabWidget(self)
        self.settings_main_tabs.setStyleSheet('''QTabBar::tab{width: 0;height: 0; margin: 0; padding: 0; border: none;}''')
        self.settings_main_tabs.addTab(self.settings_sections_tab,"")
        self.settings_main_tabs.setCurrentIndex(0)
        self.main_layout=QVBoxLayout()
        self.scroll_area=QScrollArea(self)
        self.scroll_area.setWidget(self.settings_main_tabs)
        self.scroll_area.setWidgetResizable(True)
        self.main_layout.addWidget(self.scroll_area)
        self.main_layout.setContentsMargins(0,0,0,0)
        self.setContentsMargins(0,0,0,0)
        self.setLayout(self.main_layout)
        self.setStyleSheet(styles.style_sheets.settings_style)
        #--------
    #create customization layout
    def settings_customization(self):

        #create buttons and texts
        self.change_theme_button=QPushButton("Change Theme",self)
        self.change_font_button=QPushButton("Change font",self)
        self.select_font=QComboBox(self)
        self.select_font_size=QComboBox(self)
        self.select_font.addItem("Arial")
        self.select_font_size.addItem("10")
        self.font_text=QLabel("Font : ",self)
        #------------------------

        #create main widget and main layout
        self.settings_customization_widget=QWidget(self)
        self.grid=QGridLayout(self)
        self.grid.addWidget(self.font_text,0,0)
        self.grid.addWidget(QLabel("",self),0,1)
        self.grid.addWidget(self.select_font,0,2,1,2)
        self.grid.addWidget(self.select_font_size,0,4)
        self.grid.addWidget(self.change_font_button,0,5,1,2)
        self.grid.addWidget(self.change_theme_button,1,0,1,7)
        self.settings_customization_widget.setLayout(self.grid)
        #----------------------------------

        
        return self.settings_customization_widget
    
    #create notification layout
    def settings_notification(self):

        #create buttons and texts
        self.change_sending_time_text=QLabel("Change sending time : ",self)
        self.change_sending_time_button=QDateEdit(self)
        self.change_sending_time_submit_button=QPushButton("Change time",self)
        #------------------------

        #create main widget and main layout
        self.settings_notification_widget=QWidget(self)
        self.grid1=QGridLayout(self)
        self.grid1.addWidget(self.change_sending_time_text,0,0,1,2)
        self.grid1.addWidget(self.change_sending_time_button,0,5,1,2)
        self.grid1.addWidget(self.change_sending_time_submit_button,1,0,1,7)
        self.settings_notification_widget.setLayout(self.grid1)
        #----------------------------------

        
        return self.settings_notification_widget
    
    #create data layout
    def settings_data(self):

        #create buttons and texts
        self.delete_all_apps_data=QPushButton("Delete all data",self)
        self.delete_all_users_data=QPushButton("Delete all users data",self)
        #------------------------

        #create main widget and main layout
        self.settings_data_widget=QWidget(self)
        self.grid2=QGridLayout(self)
        self.grid2.addWidget(self.delete_all_users_data,0,0)
        self.grid2.addWidget(self.delete_all_apps_data,0,1)
        self.settings_data_widget.setLayout(self.grid2)
        #----------------------------------

        
        return self.settings_data_widget
class setting_customization_tab(QWidget):
    def __init__(self):
        super().__init__()
        self.tab2 = self.create_main_tab()
    def create_main_tab(self):
        self.tab1_main_layout=QVBoxLayout(self)
        self.tab1_grid_layout=QGridLayout(self)
        self.tab1_header_layout=QGridLayout(self)
        self.tab1_button_layout=QHBoxLayout(self)
        self.appply_button=QPushButton("Apply",self)
        self.cancel_button=QPushButton("Cancel",self)
        self.back_button=QPushButton("",self)
        self.back_button.setIcon(QIcon('C:/Users/r/Contacts/Desktop/9thgrade_project/assets/back.png'))
        size=QSize(40,40)
        self.back_button.setIconSize(size)
        self.header=QLabel("Change Theme",self)
        self.back_button.setObjectName("back_button")
        self.tab1_header_layout.addWidget(self.back_button,0,0)
        self.tab1_header_layout.addWidget(QLabel("",self),0,1)
        self.tab1_header_layout.addWidget(QLabel("",self),0,2)
        self.tab1_header_layout.addWidget(QLabel("",self),0,3)
        self.tab1_header_layout.addWidget(QLabel("",self),0,4)
        self.tab1_header_layout.addWidget(self.header,0,5,1,2)
        self.background_color_label=QLabel("Background color : ",self)
        self.menu_background_color_label=QLabel("Menu background color : ",self)
        self.header_text_color=QLabel("Header text color : ",self)
        self.text_color=QLabel("Text color : ",self)
        self.button_background_color=QLabel("Button background color : ",self)
        self.button_border_color=QLabel("Button border color : ",self)
        self.border_color=QLabel("Border color : ",self)
        self.button_hover_color=QLabel("Button hover color : ",self)
        self.tab1_grid_layout.addWidget(self.background_color_label,0,0,1,2)
        self.tab1_grid_layout.addWidget(self.menu_background_color_label,1,0,1,2)
        self.tab1_grid_layout.addWidget(self.header_text_color,2,0,1,2)
        self.tab1_grid_layout.addWidget(self.text_color,3,0,1,2)
        self.tab1_grid_layout.addWidget(self.button_background_color,4,0,1,2)
        self.tab1_grid_layout.addWidget(self.button_border_color,5,0,1,2)
        self.tab1_grid_layout.addWidget(self.border_color,6,0,1,2)
        self.tab1_grid_layout.addWidget(self.button_hover_color,7,0,1,2)
        for i in range(8):
            self.tab1_grid_layout.addWidget(QLabel("",self),i,2,1,2)
        for i in range(8):
            self.tab1_grid_layout.addWidget(QLabel("R : ",self),i,5,1,1)
        self.rg_bline_edit=[]
        for i in range(8):
            ss=[]
            ss.append(QLineEdit(self))
            ss.append(QLineEdit(self))
            ss.append(QLineEdit(self))
            self.rg_bline_edit.append(ss)
            self.tab1_grid_layout.addWidget(self.rg_bline_edit[i][0],i,6,1,2)
            self.tab1_grid_layout.addWidget(QLabel("G : ",self),i,8,1,1)
            self.tab1_grid_layout.addWidget(self.rg_bline_edit[i][1],i,9,1,2)
            self.tab1_grid_layout.addWidget(QLabel("B : ",self),i,11,1,1)
            self.tab1_grid_layout.addWidget(self.rg_bline_edit[i][2],i,12,1,2)
        self.tab1_button_layout.addWidget(self.appply_button)
        self.tab1_button_layout.addWidget(self.cancel_button)
        self.tab1_main_layout.addLayout(self.tab1_header_layout)
        self.tab1_main_layout.addLayout(self.tab1_grid_layout)
        self.tab1_main_layout.addLayout(self.tab1_button_layout)
        self.setLayout(self.tab1_main_layout)
