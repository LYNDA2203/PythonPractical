reverse_vowels = lambda word : word[::-1] if word[0] in 'aeiouAEIOU' else word
print(reverse_vowels('Apple'))
print(reverse_vowels('local'))