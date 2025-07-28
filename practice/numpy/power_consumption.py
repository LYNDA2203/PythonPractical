'''Power Consumption Tracker
An energy company collects hourly power usage data (in kWh) for 50 households over 7 days (shape: 7 x 50 x 24).

Tasks:

Compute the daily average usage per household.

Find the hour with peak total city-wide consumption.

Identify households that used more than 10 kWh for 5 or more hours in a day.

Detect any day where power usage dropped below 1 kWh for every household.'''
import numpy as np

energy_company = np.random.uniform(0.5,15.0,(7,50,24))
print("Power Consumption of 50 household for a week:",energy_company.shape)

#compute daily average usage per hosehold
daily_avg = energy_company.mean(axis = 2)
print("Daily  power usage per household:\n", daily_avg)

#To find peak total city wide consumption
total_per_hour = np.sum(energy_company,axis =(0,1))
peak_hour = np.argmax(total_per_hour)
print(f"Peak hour: {peak_hour}, Total usage: {total_per_hour[peak_hour]:.2f} kWh")

#finding the householdthat consumps more than 10kwh for more then 5 hrs
high_usage = (energy_company > 10).sum(axis = 2)
flagged_reading = np.argwhere(high_usage >= 5)
print("Households using >10 kWh for >=5 hrs:\n", flagged_reading)

#Day where all households used < 1kwhs
lowday = []
for day in range(7):
    if np.all(energy_company[day] < 1.0):
        lowday.append(day)
print("Days were all usage < 1 kwh:",lowday)

