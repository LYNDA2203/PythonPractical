# Create a Book class with title, author, and genre.

# Input N books from user.

# Show:

# All unique authors

# All books under a selected genre (use filter()).

# Count how many books per genre (use dict + set).

from collections import Counter
class Book:
    
    def __init__(self,title,author,genre):
        self.title = title
        self.author = author
        self.genre = genre
        
    def __str__(self):
        return f"Title: {self.title} \nAuthor: {self.author} \nGenre: {self.genre}.lower"
    
N = int(input("Enter the number of books: "))
book = []

for i in range(N):
    print(f"Enter the details of Book {i+1}: ")
    title = input("Title: ")
    author = input("Author: ")
    genre = input("Genre: ").lower()
    book.append(Book(title,author,genre))
    
unique_author = set(a.author for a in book)

selected_genre = "comedy"

genre_book = list(filter(lambda book : book.genre == selected_genre , book))

genre_count = Counter(b.genre for b in book)

print("Unique authors",unique_author)

print(f"The book of {selected_genre} genre:")
if genre_book:
    for book in genre_book:
        print("-",book.author)
else:
    print("No book was found in that genre")