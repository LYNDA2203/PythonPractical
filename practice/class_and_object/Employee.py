# Problem Statement:
# Create an Employee class with:

# name, salary, years_of_service

# Bonus Rule:

# If an employee has service >= 5 years → eligible for 10% bonus

# Tasks:

# Create a list of employee objects with values

# Use filter() and lambda to get only eligible employees

# Calculate and display their bonus amount

# Output format:
# John is eligible for ₹2500 bonus.


class Employee:
    
    def __init__(self,name,salary,year_of_service):
        self.name = name
        self.salary = salary
        self.year_of_service = year_of_service
    
    def Cal_bonus(self):
        return self.salary * 0.10 
        
    def __str__(self):
        return f"Employee Name:{self.name}\nEmployee salary:{self.salary}\nEmployee Experience:{self.year_of_service}yrs "

E1 = Employee("punitha",30000,4)
E2 = Employee("Suganthan",25000,6)
E3 = Employee("Ramesh",45000,7)

employee = [E1,E2,E3]

emp = list(filter(lambda x : x.year_of_service >= 5 ,employee))

for employee in emp:
    bonus = employee.Cal_bonus()
    print(f"{employee.name} is eligible for ₹{bonus} bonus")
