class users ():
    def __init__(self):
        self.password="have not logged in yet"
        self.username="have not logged in yet"
        self.weight="have not logged in yet"
        self.height="have not logged in yet"
        self.age="have not logged in yet"
        self.gender="have not logged in yet"
        self.data_id="have not logged in yet"
        self.newest_schedule="have not logged in yet"
        self.log_in_status=False
        self.selected_schedule="none"
        self.streak=0
        self.freeze=0
        self.last_day_online = "none"
        self.last_day_streak = "none"
logged_in_user=users()