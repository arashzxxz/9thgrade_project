from PyQt5.QtSql import QSqlDatabase, QSqlQuery  
from users import current_user  
from datetime import datetime  
import os, sys
import sys
def get_menu (main_menu):
    main_menu = main_menu

def update_button(database):  
    query1 = QSqlQuery()  
    query1.prepare("""SELECT * FROM Data WHERE id = ? and number = ?""")  
    query1.addBindValue(current_user.logged_in_user.data_id)  
    query1.addBindValue(current_user.logged_in_user.selected_schedule)  
    query1.exec_()  
    last_day_streak = query1.value(6)
    today = datetime.today()
    if isinstance(last_day_streak, str):  
        last_day_streak = datetime.strptime(last_day_streak, '%Y-%m-%d')
    if last_day_streak == today :
        main_menu.streak_button.setStyleSheet("image: url(C:/Users/r/Contacts/Desktop/9thgrade_project/assets/streak_done.png);")
    else :
        main_menu.streak_button.setStyleSheet("image: url(C:/Users/r/Contacts/Desktop/9thgrade_project/assets/streak_undone.png);")
    
