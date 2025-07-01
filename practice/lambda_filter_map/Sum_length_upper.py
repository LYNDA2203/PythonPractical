sample_names = ['sally', 'Dylan', 'rebecca', 'Diana', 'Joanne', 'keith']

sample_names = list(filter(lambda x: x[0].isupper() and x[1:].islower(),sample_names))
print("Sum of length of string:")
print(len(''.join(sample_names)))