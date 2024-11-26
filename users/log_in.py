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
    query1.prepare("""SELECT * FROM data WHERE Username = ? AND Password = ?""")
    query1.addBindValue(username)
    query1.addBindValue(h_password)
    query1.exec_()
    if not query1.next():
        return "404"
    else :
        # get the users info
        current_user.logged_in_user.password=password
        current_user.logged_in_user.h_password=h_password
        current_user.logged_in_user.username=username
        current_user.logged_in_user.log_in_status=True
        logged_in_tab.username.setText(current_user.logged_in_user.username)
        tabs.setCurrentIndex(2)
        return "0"
        #-----------
#--------------------------------
    