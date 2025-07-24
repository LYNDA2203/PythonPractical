'''Temperature Sensor Data Analysis
You are working with an IoT team that collects hourly temperature data from sensors installed in a city. You receive a NumPy array with temperature readings (in °C) for 30 days, sampled 24 times a day (once per hour).
Task:
Generate the simulated data (shape: 30 x 24) with values ranging from 15°C to 45°C.


Find the hottest day and coldest day (based on average temperature).


Find all hours across the month where temperature crossed 40°C.


Compute the average temperature at 2 PM (14th hour) across all 30 days.


Detect any day where the temperature stayed above 35°C for more than 5 continuous hours.'''

import numpy as np

temperature_data = np.random.uniform(15,45,(30,24))
#print(temperature_data)
print("Temperature_date: ",temperature_data.shape)

#hottest and coldest temperature of the day
daily_avg = temperature_data.mean(axis = 1)
hottest = np.argmax(daily_avg) + 1
coldest = np.argmin(daily_avg) + 1

print(f"\nHottest Day: Day {hottest} with Avg Temp {daily_avg[hottest-1]:.2f}")
print(f"Coldest Day: Day {coldest} with Avg Temp {daily_avg[coldest-1]:.2f}")

high_temp = np.where(temperature_data > 40)
print("hours where crossed temperture greater than 40c:")
for day,hour in zip(high_temp[0],high_temp[1]):
    print(f"Day {day+1}, Hour {hour}: {temperature_data[day, hour]:.2f}")
    
average_2pm = temperature_data[:,14].mean()
print(f"\nAverage Temperature at 2 PM across 30 days: {average_2pm:.2f}")

for day in range(30):
    data = temperature_data[day] > 35
    count = 0
    found = False
    if hour in data:
        if hour:
            count += 1
            if count >=6:
                found = True
                break
        else:
            count = 0
    
    if found:
        print(f"Temperature stayed above 35°C for more than 5 continuous hours.{day+1}")
    else:
        print(f"No Temperature stayed above 35°C for more than 5 continuous hours.")
        