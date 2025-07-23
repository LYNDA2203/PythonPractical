# Create an Employee class with name, dept, and salary.

# Input multiple employees dynamically.

# Use filter() to get employees with salary > ₹50,000.

# Use groupby (or a custom approach) to list employees per department.

# Sort by salary descending.

class Company:
    
    def __init__(self,name,dept,salary):
        self.name = name
        self.dept = dept
        self.salary = salary
    
    def __str__(self):
        return f"Name: {self.name} \nDepartment: {self.dept} \nSalary: {self.salary}\n------------------"
    
n=int(input("Enter the number of Employees: "))
employee = []

for i in range(n):
    print(f"\nEnter the details of Empllyee {i+1}: ")
    name = input("Name: ")
    dept = input("Department: ")
    sal = int(input("Salary: "))
    employee.append(Company(name,dept,sal))
   
    
max_salary = list(filter(lambda x : x.salary > 50000 ,employee))

from collections import defaultdict
emp_dept = defaultdict(list)#syntax: vartiable_name = defaultdict(datatype)
for emp in employee:
    emp_dept[emp.dept].append(emp)

print("\nEmployee who paid max: ")
if max_salary:
    for employee in max_salary:
        print(employee) 

else:
    print("no employee paid high salary")


for dept,emp_list in emp_dept.items():
    names = ", ".join(e.name for e in emp_list)
    print(f"{dept}:{names}")
        