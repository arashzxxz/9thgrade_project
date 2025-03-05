from PyQt5.QtSql import QSqlDatabase, QSqlQuery  
from users import current_user  
from datetime import datetime  
from calculations.calculations import string_to_list, list_to_string  
def check_increased(database, date, days):  
    query1 = QSqlQuery()  
    query1.prepare("""SELECT * FROM Data WHERE id = ? and number = ?""")  
    query1.addBindValue(current_user.logged_in_user.data_id)  
    query1.addBindValue(current_user.logged_in_user.selected_schedule)  
    query1.exec_()  
    t = 0  
    while query1.next():  
        list_status = string_to_list(query1.value(8))  
        end_date = query1.value(7)   
        if isinstance(end_date, str):  
            end_date = datetime.strptime(end_date, '%Y-%m-%d')  

        if end_date >= date:  
            if list_status[days] != "none" and t == 0:  
                t = 1  
                query_update = QSqlQuery()  
                query_update.prepare("""UPDATE User SET last_day_online = ? WHERE username = ? AND password = ?""")  
                query_update.addBindValue(current_user.logged_in_user.streak + 1)  
                query_update.addBindValue(current_user.logged_in_user.username)  
                query_update.addBindValue(current_user.logged_in_user.password)  
                query_update.exec_()  

def check_decreased(database, date):  
    query1 = QSqlQuery()  
    query1.prepare("""SELECT * FROM Data WHERE id = ? and number = ?""")  
    query1.addBindValue(current_user.logged_in_user.data_id)  
    query1.addBindValue(current_user.logged_in_user.selected_schedule)  
    query1.exec_()  
    max_end_date = datetime.min
    while query1.next():  
        end_date = query1.value(7) 
        if isinstance(end_date, str):  
            end_date = datetime.strptime(end_date, '%Y-%m-%d') 
        if end_date > max_end_date:  
            max_end_date = end_date  
    last_check_date = min(max_end_date, datetime.today())  
    start_date = query1.value(6)  
    if start_date is None:  
        print("Start date is None, cannot perform date calculations.")  
        return
    if isinstance(start_date, str):  
        start_date = datetime.strptime(start_date, '%Y-%m-%d')

    days = (last_check_date - start_date).days  

    if days != 0:  
        freezes = current_user.logged_in_user.freeze  
        days = days - freezes  
        freezes = freezes - days  
        if freezes < 0:  
            freezes = 0  
        current_user.logged_in_user.freeze = freezes  

        query_update = QSqlQuery()  
        query_update.prepare("""UPDATE User SET freeze = ? WHERE username = ? AND password = ?""")  
        query_update.addBindValue(freezes)  
        query_update.addBindValue(current_user.logged_in_user.username)  
        query_update.addBindValue(current_user.logged_in_user.password)  
        query_update.exec_()  
    if days >=0 :
      query_update = QSqlQuery()  
      query_update.prepare("""UPDATE User SET streak = ? WHERE username = ? AND password = ?""")  
      query_update.addBindValue(0)  
      query_update.addBindValue(current_user.logged_in_user.username)  
      query_update.addBindValue(current_user.logged_in_user.password)  
      query_update.exec_()    