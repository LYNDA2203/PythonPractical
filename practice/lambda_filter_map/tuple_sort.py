subject_marks = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
print("Original list of tuples:")
print(subject_marks)
sorted_list=sorted(subject_marks,key=lambda x:x[-1])
print(sorted_list)