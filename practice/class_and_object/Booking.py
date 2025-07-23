# Check Slot Availability (Overlapping Time)
# Context: Hotel/Meeting Room/Doctor Scheduler
# Given a list of bookings with start and end times, write a function to check if a new booking overlaps with existing ones.

# Input:
# existing = [(10, 11), (13, 14)]
# new = (11, 13)

# Output: Available

# new = (10.5, 11.5)
# Output: Not Available

class Booking:
    
    def __init__(self,start,end):
        self.start = start
        self.end = end
        
    def overlap(self,other):
        return not (self.end <= other.start or self.start >= other.end )
        #Booking(10,11),Booking(11,13)--self.start=10,start.end=11---other.start=11,other.end=13
class BookingManager:
    
    def __init__(self):
        self.booking = []
        
    def is_available_slot(self,newbooking):
        for booking in self.booking:
            if booking.overlap(newbooking):
                return "Not Available"
        self.booking.append(newbooking)
        return "Available"

bm = BookingManager()
bm.booking = [Booking(10,11),Booking(13,14)]
print(bm.is_available_slot(Booking(11,13)))
print(bm.is_available_slot(Booking(10.5,11.5)))
   

