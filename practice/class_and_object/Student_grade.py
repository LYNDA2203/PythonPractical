# Create a Student class with attributes name and marks.

# Use filter() and lambda to find students who scored more than 70.

# Print only their names using a loop or map().


class Student:
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
    
    def __str__(self):
        return f"Student: {self.name} Marks: {self.marks}"
    
n = int(input("Enter the Number: "))

student_marks=[]

for i in range(n):
    entry = input(f"Enter the Student {i+1} name and marks (e,g., john 55) : ")
    parts = entry.strip().split()
    name = parts[0]
    marks = int(parts[1])
    student_marks.append(Student(name,marks))
    
passed_student = list(filter(lambda x: x.marks > 70,student_marks))


passed_student.sort(key=lambda x:x.name[0])

print("Student who stored about 70:")
for student in passed_student:
    print(student)
    
    
        
        

