
# Find all unique students (use set, string splitting).

# Create a tuple list of students and the count of unique subjects they like.

# Example: ('Alice', 2) means Alice likes 2 unique subjects.

# From this, generate a final list of students who like more than one subject.

# Sort the final list alphabetically and print them in the format:

def student_subject(data):
    student_sub={}
    for entry in data:
        name,subject=entry.split(':')
        if name not in student_sub:
            student_sub[name]=set()
        student_sub[name].add(subject)
    
    subject_counts = [(name,len(subject)) for name ,subject in student_sub.items()]
    
    multiple_sub_stu= [t for t in subject_counts if t[1] > 1]
    
    multiple_sub_stu.sort(key=lambda x : x[0])
    
    for name , count in multiple_sub_stu:
        print(f"student: {name}\tSubject: {count}")
        
    
data = [
    "Alice:Math", 
    "Bob:Science", 
    "Alice:Science", 
    "Charlie:Math", 
    "Bob:Math", 
    "David:English"
]
student_subject(data)