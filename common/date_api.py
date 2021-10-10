import datetime


class GetDatetime:
    def __init__(self):
        self.get_timestamp()
        self.get_date()
        self.get_yesterday()

    def get_timestamp(self):
        timestamp = datetime.datetime.now()
        self.timestamp = timestamp
    
    def get_date(self):
        today = self.timestamp.date()
        today = today.strftime("%Y/%m/%d %H:%M:%S")
        self.today = today
    
    def get_yesterday(self):
        today = datetime.datetime.strptime(self.today, "%Y/%m/%d %H:%M:%S")
        yesterday = today + datetime.timedelta(days=-1)
        yesterday = yesterday.strftime("%Y/%m/%d %H:%M:%S")
        self.yesterday = yesterday
    
    def get_other_date(self, year, month, day, hour=0, minute=0, second=0):
        other_date = datetime.datetime(year, month, day, hour, minute, second)
        other_date = other_date.strftime("%Y/%m/%d %H:%M:%S")
        return other_date