from datetime import datetime,timedelta

class TimeBooking:
    
    def __init__(self,status,created_at):
        self.status = status
        self.created_at = created_at
        
    def booking_status(self):
        if (self.status == 'pending' and datetime.now() - self.created_at > timedelta(minutes = 10)):
            return "Booking Cancelled"
        return "Booking Confirmed"
    
tb = TimeBooking('pending', datetime.now() - timedelta(minutes=15))
print(tb.booking_status())