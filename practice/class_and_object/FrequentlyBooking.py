# Find Most Frequently Booked Slot
# Context: Gym, Meeting Room
# Input: ['10AM', '11AM', '10AM', '10AM', '11AM']

# Output: '10AM' (3 times)
from collections import Counter
class FrequentlyBooking:
    
    def __init__(self,slots):
        self.slots = slots
        
    def most_common_slots(self):
        counter = Counter(self.slots)
        return counter.most_common(1)[0]
    
fb= FrequentlyBooking(['10AM', '11AM', '10AM', '10AM', '11AM'])
print(fb.most_common_slots())