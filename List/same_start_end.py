lst=['abc','xyz','aba','1221']
count = 0
for char in lst:
    if char[0] == char[-1] and len(char) > 1:
            count += 1

print(count)