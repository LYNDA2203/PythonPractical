'''Fridge Temperature Control
You have temperature readings (°C) of 10 smart fridges taken every hour for a week (shape: 7 x 10 x 24).

Tasks:

Flag fridges that went above 8°C at any time (risking spoilage).

Compute the standard deviation of temperatures for each fridge.

Find hours of the week with the most frequent temperature spikes.

List fridges that were consistently under 4°C during daytime hours (8 AM to 8 PM).'''

import numpy as np

temp_control = np.random.uniform(2.0,10.0,(7,10,24))
print("Fridge temperature for a week every hour:",temp_control)

#finding fridge above 8°c at any time
risk_limit = np.argwhere(temp_control > 8.0)
print("Over_temperature reading:\n", risk_limit)

#computing the standand deviation of each temperature
std_temp = temp_control.std(axis =(0,2))
print("Temperature std deviation per fridge:\n",std_temp)

#hours with most frequesnt spikes
spikes = (temp_control > 8).sum(axis=(0,1))
print("Spikes count per hour:\n",spikes)
 
#fridges that were consistently under 4°C during daytime hours (8 AM to 8 PM)
consistent_fridge = []
for day in range(7):
    for fridge in range(10):
        if np.all(temp_control[day,fridge,8:20] < 4.0):
            consistent_fridge.append((day,fridge))
            
print("Fridges consistently under 4°C (8AM–8PM):", consistent_fridge)