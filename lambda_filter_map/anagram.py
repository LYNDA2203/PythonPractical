from collections import Counter
lst=['bcda', 'abce', 'cbda', 'cbea', 'adcb']

str='abcd'

print("The original list of Strings:")
print(lst)

anagram = list(filter(lambda x : Counter(str) == Counter(x),lst))
print(f"Anagrams of {str} in the above string:")
print(anagram)
