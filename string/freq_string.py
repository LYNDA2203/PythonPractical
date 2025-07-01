str1="google.com"
dict_={}
for char in str1:
    keys=dict_.keys()
    if char in keys:
        dict_[char] += 1
    else:
        dict_[char] = 1
print(dict_)
        