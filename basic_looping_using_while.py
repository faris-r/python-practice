"""
This is example of basic looping using while
"""
books_count = 10
print("Teacher asked Joe to read all of his books")

books_read = 0
print(f"The number of books that Joe has read is {books_read} book(s)")

while books_read < books_count:
    books_read = books_read + 1
    print(f"Joe read book {books_read}")

print(f"The number of books that Joe has read is {books_read} books")