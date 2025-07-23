class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.__salary = salary #private
        
    #Getter using @property
    @property
    def set_salary(self):
        return self.__salary
    
    #setter for setting the salary
    @set_salary.setter
    def salary(self,amount):
        try: 
            if amount > 0:
                self.__salary = amount
                print(f"Salary update to : ₹{amount}")
            else:
                raise ValueError("Salary must be positive!!!")
        except ValueError as e:
            print(f"Error: {e}")
            
    def display_info(self):
        print(f"Employee: {self.name}")
        print(f"current Salary: ₹{self.__salary}")
    
emp = Employee("lynda",30000)
emp.display_info()

emp.salary = 60000
emp.salary = -10000

emp.display_info()