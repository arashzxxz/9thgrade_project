
import sys
import main
import hashlib
from PyQt5.QtSql import QSqlDatabase,QSqlQuery
from PyQt5.QtCore import Qt,QTime,QTimer,QDate,QSize
from PyQt5.QtGui import QFontDatabase,QStandardItemModel,QStandardItem
def sign_in_backend(username,password,database):
# hash the password
    h=hashlib.new("SHA256")
    h.update(password.encode())
    h_password=h.hexdigest()
#------------------

#check if user is already created
    query1=QSqlQuery()
    query1.prepare("""SELECT * FROM data WHERE Username = ? AND Password = ?""")
    query1.addBindValue(username)
    query1.addBindValue(h_password)
    query1.exec_()
    if query1.next():
        return 409
    else :
        # create user
        query2=QSqlQuery()
        query2.prepare("""INSERT INTO data (Username, Password)VALUES (?, ?)""")
        query2.addBindValue(username)
        query2.addBindValue(h_password)
        query2.exec_()
        return 0
        #-----------
#--------------------------------
    