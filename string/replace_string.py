str1=input("Enter the string : ")
str2=str1[0]
replaced_string=str2+str1[1:].replace(str2,'$')
print(replaced_string)
    