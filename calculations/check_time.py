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

notification_thread = None
def send_notification():  
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

def check_local_time(database, notification_time, check_type):  
    timezone = get_local_timezone()  
    if timezone is None:  
        return   

    while True:  
        local_time = datetime.now(pytz.timezone(timezone))  
        if check_type == 2:  
            if local_time.hour >= notification_time:  
                set_undone_states(database)   
        elif check_type == 1:  
            if local_time.hour == notification_time and local_time.minute == 0:  
                send_notification()  

        time.sleep(60)  

def start_background_task_undone(database):  
    scheduler_thread = threading.Thread(target=check_local_time, args=(database, 24, 2))  
    scheduler_thread.daemon = True  
    scheduler_thread.start()  

def start_background_task_notification(database, notification_time):  
    scheduler_thread = threading.Thread(target=check_local_time, args=(database, notification_time, 1))  
    scheduler_thread.daemon = True  
    scheduler_thread.start()  

def stop_existing_notification_thread():  
    global notification_thread  
    if notification_thread is not None and notification_thread.is_alive():  
        print("Stopping existing notification thread.")  
        notification_thread = None

def set_notification_time(database,new_time):  
    if 0 <= new_time < 24:  
        stop_existing_notification_thread()  
        start_background_task_notification(database, new_time)  
    else:  
        print("Invalid notification time. Please enter an hour between 0 and 23.")  

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