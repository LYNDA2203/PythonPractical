# You need to:

# Create a Person class with:

# name

# hobbies (a list of strings)

# Store at least 5 people with their hobbies (some hobbies can repeat across people).

# Find and display all unique hobbies (no duplicates).

# Display the person with the most hobbies.

class Person:
    
    def __init__(self,name,hobbies):
        self.name = name
        self.hobbies = hobbies
    
    def __str__(self):
        return f"Person {self.name} and their hobbies {','.join(self.hobbies)}"
    
p1 = Person("Alice", ["Reading", "Painting", "Gardening"])
p2 = Person("Bob", ["Gaming", "Cooking", "Reading"])
p3 = Person("Priya", ["Dancing", "Gardening", "Singing"])
p4 = Person("Ravi", ["Swimming", "Gaming"])
p5 = Person("Neha", ["Painting", "Blogging", "Dancing", "Cooking"])

people = [p1,p2,p3,p4,p5]

all_hobbies = set()

for person in people:
    all_hobbies.update(person.hobbies)
    
max_hobbies=max(people,key=lambda p: len(p.hobbies))

print("All unique hobbies:")
for hobby in all_hobbies:
    print("-",hobby)
    
print(f"{max_hobbies.name} has the max hobbies: {len(max_hobbies.hobbies)}")
print(f"hobbies are {','.join(max_hobbies.hobbies)}")       