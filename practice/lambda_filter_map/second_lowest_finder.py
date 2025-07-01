n = int(input("Input number of students: "))
students=[]

for i in range(n):
    name = input("Name: ").strip()
    grade = float(input("Grade: "))
    students.append([name,grade])
    
print("Name and Grade of all students:")
print(students)

grades=sorted(set(map(lambda x: x[1],students)))

second_lowest=grades[1]
print(f"second lowest grade: {second_lowest}")

second_lowest_student = sorted(filter(lambda x:x[1] == second_lowest , students),key = lambda x:x[0])

print("Names:")
for student in second_lowest_student:
    print(student[0])