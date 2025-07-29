'''Patient_ID	Name	Department	Condition	Admission_Date	Discharge_Date
P001	John	Cardiology	Stable	2024-05-01	2024-05-10
P002	Alice	Neurology	Critical	2024-05-03	2024-05-20
P003	Michael	Cardiology	Critical	2024-05-04	2024-05-14
P004	Lisa	Oncology	Stable	2024-05-05	2024-05-18
...	...	...	...	...'''
import pandas as pd

#load deatil from xlsx and displaying the first 5 records
patient_details = pd.read_csv("hospital_patient_data.csv",sep = '\t')
print(patient_details.head()) 

#patient in each department
patient_count = patient_details['Department'].value_counts()
print(f"\nNumber of patients Each department: \n{patient_count}")

#patient in critical condition
critical = patient_details[patient_details['Condition'] == 'Critical']
print(f"\nCritical Condition:\n {critical}")

#patient stay in the hospital
patient_details['Admission_Date'] = pd.to_datetime(patient_details['Admission_Date'], errors='coerce')
patient_details['Discharge_Date'] = pd.to_datetime(patient_details['Discharge_Date'], errors='coerce')

patient_details['Stay_days'] = (patient_details['Discharge_Date'] - patient_details['Admission_Date']).dt.days
print(patient_details)

#average hospital stay
avg_stay = patient_details['Stay_days'].mean()
print(f"Average Stay: {avg_stay:.2f} days")

#longest stay in the hospital
longest_stay_index = patient_details['Stay_days'].idxmax()
longest_stay_patient = patient_details.loc[longest_stay_index]
print(f"\npateient with Longest stay :\n",longest_stay_patient)

#Adding the new coloumn 'Status'

patient_details['Status'] = patient_details['Stay_days'].apply(lambda x: 'Long Stay' if x > 10 else 'Short Stay')
print(f"\n{patient_details}\n")