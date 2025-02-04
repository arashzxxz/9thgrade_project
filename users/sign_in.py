
import sys
import main
import hashlib
import random as rd
from PyQt5.QtSql import QSqlDatabase,QSqlQuery
from PyQt5.QtCore import Qt,QTime,QTimer,QDate,QSize
from PyQt5.QtGui import QFontDatabase,QStandardItemModel,QStandardItem
def sign_in_backend(username,password,database):
# hash the password
    h=hashlib.new("SHA256")
    h.update(password.encode())
    h_password=h.hexdigest()
#------------------

#create and check the data_id
    def create_and_check_data_id():
        temporary_id=rd.randint(0,int(1e6))
        h=hashlib.new("SHA256")
        h.update(str(temporary_id).encode())
        h_temporary_id=h.hexdigest()
        check_query=QSqlQuery()
        check_query.prepare("""SELECT * FROM Data WHERE id = ?""")
        check_query.addBindValue(h_temporary_id)
        check_query.exec_()
        if check_query.next():
            create_and_check_data_id()
        else :
            return temporary_id
#---------------------------

#check if user is already created
    query1=QSqlQuery()
    query1.prepare("""SELECT * FROM User WHERE username = ? AND password = ?""")
    query1.addBindValue(username)
    query1.addBindValue(h_password)
    query1.exec_()
    if query1.next():
        return "409"
    else :
        # create user
        data_id=create_and_check_data_id()
        query2=QSqlQuery()
        query2.prepare("""INSERT INTO User (username, password, data_id)VALUES (?, ?, ?)""")
        query2.addBindValue(username)
        query2.addBindValue(h_password)
        query2.addBindValue(data_id)
        query2.exec_()
        
        return "0"
        #-----------
#--------------------------------
    