import time  
import threading  
from datetime import datetime  
from geopy.geocoders import Nominatim  
from timezonefinder import TimezoneFinder  
import pytz  
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
def check_local_time():  
    timezone = get_local_timezone()  
    if timezone is None:  
        return  
    while True:  
        local_time = datetime.now(pytz.timezone(timezone))  
        if local_time.hour >= 24:  
            print(f"The local time is {local_time.strftime('%H:%M')} - The hour is past 12 PM.")  
        else:  
            print(f"The local time is {local_time.strftime('%H:%M')} - It is before 12 PM.")  
        time.sleep(300)  
def start_background_task():  
    scheduler_thread = threading.Thread(target=check_local_time)  
    scheduler_thread.daemon = True  
    scheduler_thread.start()  
