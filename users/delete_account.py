import sys
import main
import hashlib
from users import current_user
from PyQt5.QtSql import QSqlDatabase,QSqlQuery
from PyQt5.QtCore import Qt,QTime,QTimer,QDate,QSize
from PyQt5.QtGui import QFontDatabase,QStandardItemModel,QStandardItem
def delete_account_backend(database):
# hash the password
    password=current_user.logged_in_user.password
    username=current_user.logged_in_user.username
    h=hashlib.new("SHA256")
    h.update(password.encode())
    h_password=h.hexdigest()
#------------------
#delete the user
    query2=QSqlQuery()
    query2.prepare("""DELETE FROM User WHERE username = ? AND password = ?""")
    query2.addBindValue(username)
    query2.addBindValue(h_password)
    query2.exec_()
    return "0"
#-------------
