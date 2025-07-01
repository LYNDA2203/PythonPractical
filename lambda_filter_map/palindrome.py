words = ['madam', 'racecar', 'python', 'level', 'data']
pal=list(filter(lambda w : w[::-1] == w ,words))
print(pal)