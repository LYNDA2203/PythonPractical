'''River Water Level Analysis
You receive water level data collected every 30 minutes over 15 days for a river (shape: 15 x 48).

Tasks:

Find the day with the highest average water level.

Check if water level crossed a critical threshold (e.g., 9.5 m) at any point.

Determine peak water level time for each day.

Identify days where the water level rose continuously for 6 or more intervals.'''

import numpy as np

water_level = np.random.uniform(5.0,10.0,(15,48))
print("River water level shape:",water_level.shape)

#calculating high averge water level
avg_water_level = water_level.mean(axis = 1)
high_day =np.argmax(avg_water_level)
print(f"Day with highest average water level: Day {high_day}, Level: {avg_water_level[high_day]:.2f}m")

#checking water level crosses the critical level
critical_level = np.argwhere(water_level > 9.5)
print("Points where water level exceeded 9.5m:\n", critical_level)

#finding the peak water level for each day
peak_time = np.argmax(water_level,axis = 1)
print("Peak reading time (0–47) per day:\n", peak_time)

rising_days = []
for time,day in enumerate(water_level):
    count = 0
    for level in range(1,len(day)):
        if day[level] > day[level-1]:
            count += 1
            if count >=6:
                rising_days.append(time)
                break
            
        else:
            count = 0
            
print("Days with 6 continuous rising water levels:", rising_days)