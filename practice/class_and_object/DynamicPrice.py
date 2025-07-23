class DynamicPrice:
    
    def __init__(self,base_price=1000):
        self.base_price = base_price
        
    def dynamic_price_user(self,is_weekend,room_left,vip):
        price = self.base_price
        
        if is_weekend:
            price *= 1.2
            
        if room_left < 3:
            price *= 1.3
        
        if vip:
            price *= .9

        return round(price)
            
dp = DynamicPrice()
print(dp.dynamic_price_user(is_weekend= True,room_left=2,vip=True))
