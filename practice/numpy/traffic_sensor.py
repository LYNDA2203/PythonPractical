'''Traffic Sensor Data
Hourly car counts from a major intersection over 14 days (shape: 14 x 24).

Tasks:

Identify rush hours based on average hourly traffic.

Find the day with least traffic.

Calculate total weekly traffic.

Detect patterns: Are weekends busier than weekdays?

'''

import numpy as np

traffic_count = np.random.randint(100,1000,(14,24))
print("Hourly calculation of the car in traffic:",traffic_count.shape)

#Identify rush hours based on average hourly traffic
hourly_avg = traffic_count.mean(axis = 0)
rush_hour = np.argmax(hourly_avg)
print(f"Rush Hour: {rush_hour}, Average Count:{hourly_avg[rush_hour]:.2f}")

#Find the day with least traffic.
daily_total = traffic_count.sum(axis = 1)
quiet_day = np.argmin(daily_total)
print(f"least traffic Day : {quiet_day},Total cars: {daily_total[quiet_day]:.2f}")

#Calculate total weekly traffic.
total_traffic = traffic_count.sum()
print("Total 2_week traffic:",total_traffic)

#weekend Vs Weekday comparison
weekend = [5,6,12,13]# if monday =0
weekday = [day for day in range(14) if day not in weekend]
weekend_avg = traffic_count[weekend].mean()
weekday_avg = traffic_count[weekday].mean()
print(f"Weekend Avg: {weekend_avg:.2f},Weekday Avg: {weekday_avg}")

