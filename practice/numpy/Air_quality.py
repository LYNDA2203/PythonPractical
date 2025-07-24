'''Air Quality Monitoring System
You receive an array representing hourly AQI (Air Quality Index) data from sensors placed across 10 locations in a city, over 7 days (shape: 7 x 10 x 24).

Tasks:

Find the location with the worst average air quality for the week.

Determine the number of hours AQI exceeded 200 (poor air) at each location.

Calculate the average AQI for each hour of the day across all locations and days.

Identify any location where AQI stayed below 50 (good air) for an entire day.'''
import numpy as np

air_condition = np.random.uniform(40,200,(7,10,24))
#print(air_condition) 
print("Air Quality Monitior shape:",air_condition.shape)

avg_aqi = air_condition.mean(axis = (0,2))
worst_location=np.argmax(avg_aqi)
print(f"Worst average AQI: Location {worst_location}, AQI: {avg_aqi[worst_location]:.2f}")

high_pollution_counts = (air_condition > 200).sum(axis=2)
print("High AQI hours (AQI > 200) each day per location:\n", high_pollution_counts)

hourly_avg=air_condition.mean(axis=(0,1))
print("Hourly average AQI across all locations and days:\n", hourly_avg)

good_days = []
for day in range(7):
    for loc in range(10):
        if np.all(air_condition[day,loc] < 50):
            good_days.append((day,loc))
print("Days and locations with AQI < 50 for entire day:", good_days)