class Students:
    def __init__(self,name,stu_id,grade):
        self.name = name
        self.__stu_id = stu_id
        self.__grade = grade
     
     #getter and setter for student_id   
    def get_student_id(self):
        return self.__stu_id
    
    def set_student_id(self,new_id):
        if len(str(new_id)) == 4:
            self.__stu_id == new_id
        else:
            print("ID must be 4 digits..")
            
    #getters and setters for grade
    def get_grade(self):
        return self.__grade
    
    def set_grade(self,grade):
        if grade in ['A','B','C','D','F']:
            self.__grade = grade
        else:
            print("Invalid grade.")
        
s = Students("kholi",1023,'B')
print("Student Id:",s.get_student_id())
print("Grade: ",s.get_grade())

s1 = Students("kali",20412,"E")
print("Student Id:",s1.get_student_id())
print("Grade: ",s1.get_grade())

s1.set_grade('E')
s1.set_student_id(20345)