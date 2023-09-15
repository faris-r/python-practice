"""
This is example of basic looping using while w/ undefined count
with limitation variable
"""
books_count = 10
print("Teacher asked Joe to read & understand all of his books")
total_read = 0
books_read_understood = 0
print(f"The number of books Joe has read & understood is {books_read_understood}")
while total_read < books_count * 2:
    total_read = total_read + 1
    if books_read_understood == 9:
        print(f"Joe hasn't understood book {books_read_understood + 1}")
    else:
        books_read_understood = books_read_understood + 1
        print(f"Joe has read & understood book {books_read_understood}")
print(f"The number of books Joe has read & understood is {books_read_understood}")
if books_read_understood == books_count:
    print("Mam, I've already read & understood all 10 books")
else:
    print(f"Mam, I've only read & understood {books_read_understood} book(s)")