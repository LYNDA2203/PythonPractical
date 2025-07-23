#  Waitlist Promotion
# Context: Train/Hotel/Flight
# waitlist = ['user1', 'user2', 'user3']
# canceled_booking = 'userX'

# → user1 is moved from waitlist to confirmed list
class WaitlistPromotion:
    
    def __init__(self,user):
        self.waitlist = user
        
    def ispromote(self):
        if self.waitlist: 
            return self.waitlist.pop(0)
        return None
    
wp = WaitlistPromotion(['user1','user2','user3'])
print(f"Promoted:",wp.ispromote())
print(f"REmaining:",wp.waitlist)
    