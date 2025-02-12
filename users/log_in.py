import sys
import main
import hashlib
from users import current_user
from PyQt5.QtSql import QSqlDatabase,QSqlQuery
from PyQt5.QtCore import Qt,QTime,QTimer,QDate,QSize
from PyQt5.QtGui import QFontDatabase,QStandardItemModel,QStandardItem
def log_in_backend(username,password,database,tabs,logged_in_tab):
# hash the password
    h=hashlib.new("SHA256")
    h.update(password.encode())
    h_password=h.hexdigest()
#------------------

#check if user exists

    query1=QSqlQuery()
    query1.prepare("""SELECT * FROM User WHERE username = ? AND password = ?""")
    query1.addBindValue(username)
    query1.addBindValue(h_password)
    query1.exec_()
    if not query1.next():
        return "404"
    else :
        # get the users info
        data_id_wh=str(query1.value(0))
        data_query=QSqlQuery()
        data_query.prepare("""SELECT * FROM Data WHERE id = ?""")
        data_query.addBindValue(data_id_wh)
        data_query.exec_()
        current_user.logged_in_user.password=password
        current_user.logged_in_user.username=username
        current_user.logged_in_user.log_in_status=True
        current_user.logged_in_user.weight=data_query.value(1)
        current_user.logged_in_user.height=data_query.value(2)
        current_user.logged_in_user.age=data_query.value(3)
        current_user.logged_in_user.gender=data_query.value(4)
        current_user.logged_in_user.data_id=data_id_wh
        query1=QSqlQuery()
        query1.prepare("""SELECT * FROM Data WHERE id = ? ORDER BY number DESC""")
        query1.addBindValue(data_id_wh)
        query1.exec_()
        if query1.next():
            number=query1.value(9)
        else:
            number=-1
        current_user.logged_in_user.newest_schedule=int(number)
        logged_in_tab.username.setText(current_user.logged_in_user.username)
        logged_in_tab.weight.setText(current_user.logged_in_user.weight)
        logged_in_tab.height1.setText(current_user.logged_in_user.height)
        logged_in_tab.age.setText(current_user.logged_in_user.age)
        logged_in_tab.gender.setText(current_user.logged_in_user.gender)
        return "0"
        #-----------
#--------------------------------
    