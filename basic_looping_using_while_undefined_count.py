"""
This is example of basic looping using while w/ undefined count
"""
books_count = 10
print("Teacher asked Joe to read & understand all of his books")

books_read_and_understood = 0
print(f"The number of books that Joe has read is {books_read_and_understood} book(s)")

while books_read_and_understood < books_count:
    if books_read_and_understood == 9:
        print(f"Joe hasn't understood book {books_read_and_understood + 1}")
    else:
        books_read_and_understood = books_read_and_understood + 1
        print(f"Joe has read & understood book {books_read_and_understood}")

print(f"The number of books that Joe has read is {books_read_and_understood} books")