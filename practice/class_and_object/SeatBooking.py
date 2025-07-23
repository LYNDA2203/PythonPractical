class SeatBooking:
    
    def __init__(self,booking_seat):
        self.booking_seat = set(booking_seat)
        
    def is_available(self,request):
        return [seat for seat in request if seat not in self.booking_seat]

sb = SeatBooking(['A1','A2'])
print(f"The Seat Available: ",sb.is_available(['A3','A1']))