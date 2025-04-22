from PyQt5.QtSql import QSqlDatabase,QSqlQuery
def set_state(database,obj,sender):
    state = sender

    if state == "none":
        obj.set_mode_none()
    elif state == "done":
        obj.set_mode_done()
    elif state == "undone":
        obj.set_mode_undone()
    elif state == "perfect":
        obj.set_mode_perfect()
