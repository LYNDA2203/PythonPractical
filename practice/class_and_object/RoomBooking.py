# Hotel Room Booking System
# Concepts: Composition, Date handling, Availability logic
#  Problem:
# Classes: Room, Customer, Booking, Hotel


# Book a room based on availability
class RoomBooking:
    
    def __init__(self,room):
        self.room = room
        self.booked = []
    
    def room_nearby(self):
        for rooms in sorted(self.room):
            if rooms not in self.booked:
                self.booked.append(rooms)
                return rooms
        return "No room available"
    
rb=RoomBooking([101,104,103,102])
rb.booked=[101,104]
print(f"Room nearby:",rb.room_nearby())

        
        