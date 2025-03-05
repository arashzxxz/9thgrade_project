import time  
import threading  
from datetime import datetime, timedelta   
from geopy.geocoders import Nominatim  
from timezonefinder import TimezoneFinder  
from PyQt5.QtSql import QSqlDatabase, QSqlQuery  
from users import current_user  
from data.check_streak import check_decreased  
from calculations.calculations import list_to_string, string_to_list  
import pytz  
from plyer import notification  

def send_notification():  
    # Send a notification  
    notification.notify(  
        title="Time Alert",  
        message="Don't forget to do your lessons",  
        app_name="Notification App",  
        timeout=10  
    )  

def get_local_timezone():  
    geolocator = Nominatim(user_agent="timezone_checker")  
    location = geolocator.geocode("Your Location")  
    if location is not None:  
        latitude = location.latitude  
        longitude = location.longitude  
        print(f"Detected location: {location.address}")  
        tf = TimezoneFinder()  
        timezone = tf.timezone_at(lat=latitude, lng=longitude)  
        return timezone  
    else:  
        print("Could not determine location. Using UTC as default.")  
        return 'UTC'  

def check_local_time(database, time2, c):  
    timezone = get_local_timezone()  
    if timezone is None:  
        return   

    while True:  
        local_time = datetime.now(pytz.timezone(timezone))  
        if c == 2:  
            if local_time.hour >= time2:  
                set_undone_states(database)   
        elif c == 1:  
            if local_time.hour == time2 and local_time.minute == 0:  
                send_notification()  

        time.sleep(300)  

def start_background_task_undone(database):  
    scheduler_thread = threading.Thread(target=check_local_time, args=(database, 24, 2))  
    scheduler_thread.daemon = True  
    scheduler_thread.start()  

def start_background_task_notification(database, time2):  
    scheduler_thread = threading.Thread(target=check_local_time, args=(database, time2, 1))  
    scheduler_thread.daemon = True  
    scheduler_thread.start()  

def set_undone_states(database):  
    query_undone_days = QSqlQuery()  
    query_undone_days.prepare("""SELECT * FROM data WHERE id = ? ORDER BY number""")  
    query_undone_days.addBindValue(current_user.logged_in_user.data_id)  
    query_undone_days.exec_()   

    while query_undone_days.next():  
        last_day_date = query_undone_days.value(7)  
        first_day_date = query_undone_days.value(6)  
        last_day_date = datetime.strptime(last_day_date, "%Y-%m-%d")   
        first_day_date = datetime.strptime(first_day_date, "%Y-%m-%d")   
        number = query_undone_days.value(9)  
        current_date = datetime.today()  
        yesterday = current_date - timedelta(days=1)  
        
        if yesterday <= last_day_date:   
            list_state = string_to_list(query_undone_days.value(8))  
            days = (yesterday - first_day_date).days  
            if list_state[days] == "none":  
                list_state[days] = "undone"  

                query_update = QSqlQuery()  
                query_update.prepare("""UPDATE data SET data_days_state = ? WHERE id = ? AND number = ?""")  
                query_update.addBindValue(list_to_string(list_state))  
                query_update.addBindValue(current_user.logged_in_user.data_id)  
                query_update.addBindValue(number)  
                query_update.exec_()   
                check_decreased(database, datetime.today())  