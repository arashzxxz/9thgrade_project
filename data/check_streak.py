import os
from PyQt5.QtSql import QSqlDatabase, QSqlQuery  
from users import current_user  
from datetime import datetime 
from assets.assests import get_assets_working_dir 
from calculations.calculations import string_to_list, list_to_string  
def check_increased(database, date, days,button):   
    
    query = QSqlQuery()  
    query.prepare("""SELECT * FROM Data WHERE id = ? AND number = ?""")  
    query.addBindValue(current_user.logged_in_user.data_id)  
    query.addBindValue(current_user.logged_in_user.selected_schedule)  
    
    if not query.exec_():  
        print("Query execution failed")  
        return  
    
    t = 0  
    while query.next():  
        list_status = string_to_list(query.value(8))  
        end_date = query.value(7)  

        if isinstance(end_date, str):  
            end_date = datetime.strptime(end_date, '%Y-%m-%d')  
        
        if end_date >= date:  
            if list_status[days] != "none" and t == 0:  
                t = 1  
                streak_increment_update = QSqlQuery()  
                streak_increment_update.prepare("""UPDATE User SET last_day_streak = ?, streak = ? WHERE username = ? AND password = ?""")  
                streak_increment_update.addBindValue(str(datetime.today()))  
                current_user.logged_in_user.last_day_streak = datetime.today()
                if not current_user.logged_in_user.streak :
                    current_user.logged_in_user.streak = 0
                streak_increment_update.addBindValue(current_user.logged_in_user.streak + 1)  
                streak_increment_update.addBindValue(current_user.logged_in_user.username)  
                streak_increment_update.addBindValue(current_user.logged_in_user.password)  
                
                if not streak_increment_update.exec_():  
                    print("Failed to update streak")  
                    return  
                
                current_user.logged_in_user.streak += 1  

    if t == 1:
        button.setStyleSheet("""
        QRadioButton#streakb::indicator::unchecked{
                        image: url(C:/Users/r/Contacts/Desktop/9thgrade_project/assets/streak_done.png);
                        
        }
        QRadioButton#streakb::indicator::checked{
                        image: url(C:/Users/r/Contacts/Desktop/9thgrade_project/assets/streak_done.png);
                        
        }""")  

def check_decreased(database, date):  
    query = QSqlQuery()  
    query.prepare("""SELECT * FROM Data WHERE id = ? AND number = ?""")  
    query.addBindValue(current_user.logged_in_user.data_id)  
    query.addBindValue(current_user.logged_in_user.selected_schedule)  
    
    if not query.exec_():  
        print("Query execution failed")  
        return  

    max_end_date = datetime.min  
    start_date = None  
    
    while query.next():  
        end_date = query.value(7)  

        if isinstance(end_date, str):  
            end_date = datetime.strptime(end_date, '%Y-%m-%d')  
        
        if end_date > max_end_date:  
            max_end_date = end_date  
        
        start_date = query.value(6)  

    if start_date is None:  
        print("Start date is None, cannot perform date calculations.")  
        return  

    if isinstance(start_date, str):  
        start_date = datetime.strptime(start_date, '%Y-%m-%d')  

    last_check_date = min(max_end_date, datetime.today())  
    days_difference = (last_check_date - start_date).days  

    if days_difference != 0:  
        freezes = current_user.logged_in_user.freeze  
        days_difference -= freezes  
        freezes -= days_difference  
        
        current_user.logged_in_user.freeze = max(freezes, 0)  

        freeze_update = QSqlQuery()  
        freeze_update.prepare("""UPDATE User SET freeze = ? WHERE username = ? AND password = ?""")  
        freeze_update.addBindValue(current_user.logged_in_user.freeze)  
        freeze_update.addBindValue(current_user.logged_in_user.username)  
        freeze_update.addBindValue(current_user.logged_in_user.password)  
        
        if not freeze_update.exec_():  
            print("Failed to update freeze")  
            return  

    if days_difference >= 0:  
        streak_reset_update = QSqlQuery()  
        streak_reset_update.prepare("""UPDATE User SET streak = ? WHERE username = ? AND password = ?""")  
        streak_reset_update.addBindValue(0)  
        streak_reset_update.addBindValue(current_user.logged_in_user.username)  
        streak_reset_update.addBindValue(current_user.logged_in_user.password)  
        
        if not streak_reset_update.exec_():  
            print("Failed to reset streak")  