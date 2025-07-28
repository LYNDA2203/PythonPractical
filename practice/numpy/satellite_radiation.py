''' Satellite Radiation Monitoring
You receive radiation sensor data every hour over a grid of 5x5 zones for 3 days (shape: 3 x 5 x 5 x 24).

Tasks:

Compute mean radiation for each zone over 3 days.

Highlight zones with readings over a safety limit (e.g., > 150 units).

Find zones where radiation remained above 100 for 10 continuous hours.

Generate a heatmap of average hourly radiation across all zones.

'''
import numpy as np

sensor_data = np.random.uniform(80,200,(3,5,5,24))
print("The radiation sensor data for every hour:",sensor_data.shape)

#Compute mean radiation for each zone over 3 days.
zone_mean = sensor_data.mean(axis = (0,3))
print(f"Average radiaton perZon (5*5 grid):\n",zone_mean)

#zones over safety limit(>150)
unsafe_zones = np.argwhere(sensor_data > 150)
print("Unsafe radiation values found at:\n",unsafe_zones)

def has_10hrs_streak(data,threshold = 100):
    count = 0
    for val in data:
        if val > threshold:
            count += 1
            if count >= 10:
                return True
            
        else:
            count = 0
    return False

alert_zones = []
for day in range(3):
    for strike in range(5):
        for strikes in range(5):
            if has_10hrs_streak(sensor_data[day,strike,strikes]):
                alert_zones.append((day,strike,strikes))

print("Zones with radiation >100 for 10+ continuous hours:\n", alert_zones)

#heatmap of average hourly radiation across all zones
avg_hourly_radiation = sensor_data.mean(axis = 3)
print("Hourly average radiation(3 days,585 zones):\n",avg_hourly_radiation)
