
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
    query1.prepare("""SELECT * FROM data 
                 WHERE Username = ?""")
    query1.addBindValue(h_password)
    query1.exec_()
    print(query1.value(0))
#--------------------------------
    