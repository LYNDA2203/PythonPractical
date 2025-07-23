class Person:
    def __init__(self,name):
        self.name = name

#single inheritance
class Employee(Person):
    def __init__(self, name,salary):
        super().__init__(name)
        self.salary = salary

class Job:
    def __init__(self,salary):
        self.salary = salary

#multiple inheritance        
class EmployeePersonJob(Employee,Job):
    def __init__(self, name, salary):
        Employee.__init__(self,name, salary)
        Job.__init__(self,salary)

#multilevel inheritance
class Manager(EmployeePersonJob):
    def __init__(self, name, salary,department):
        EmployeePersonJob.__init__(self,name, salary)
        self.department = department
        
#Hierarchical Inheritance
class AssistantManager(EmployeePersonJob):
    def __init__(self, name, salary,team_size):
        EmployeePersonJob.__init__(self,name, salary)
        self.team_size = team_size
        
#hydrid Inheritance(multiple + multilevel)
class SeniorManager(Manager,AssistantManager):
    def __init__(self, name, salary, department,team_size):
        Manager.__init__(self,name, salary, department)
        AssistantManager.__init__(self,name,salary,team_size)
        
emp = Employee("lynda" ,30000)
print(emp.name,emp.salary)

#multiple inheritance
emp1 = EmployeePersonJob("Geroge",50000)
print(emp1.name,emp1.salary)

#multilevel Inheritance
mgr = Manager("Anu",60000,"HR")
print(mgr.name,mgr.salary,mgr.department)

#Hierarchical Inheritance
asst_mgr = AssistantManager("Deju",45000,10)
print(asst_mgr.name,asst_mgr.salary,asst_mgr.team_size)

#Hybrid Inheritance
sen_mgr = SeniorManager("David",700000,"Finance",20)
print(sen_mgr.name,sen_mgr.salary,sen_mgr.department,sen_mgr.team_size)