"""
This is the first demo for basic looping program for reading books
"""
books_count = 10
print("Teacher asked Joe to read all of his books")

books_read = 0
print(f"The number of books read is {books_read}")

for books_read in range(1,books_count + 1):
    print(f"Joe reads book {books_read}")

print(f"Total read books is {books_read}")