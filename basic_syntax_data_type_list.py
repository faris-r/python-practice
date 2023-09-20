book_list = ['One Piece', 'Das Capital', '1984']
print('Show variable book_list')
print(book_list)

print('\nShow all variable book_list with for in')
for book in book_list:
    print(book)

print('\nShow book_list content at certain index')
print(book_list[0])
print(book_list[2])

print('\nShow book_list content with for in range')
for i in range(0, len(book_list)):
    print(book_list[i])

print('\nAdding 1 new book title')
book_list.append('Bleach')
for i in range(0, len(book_list)):
    print(book_list[i])

print('\nClear List')
book_list.clear()
for i in range(0, len(book_list)):
    print(book_list[i])

book_list = ['One Piece', 'Das Capital', '1984']
print('\nReplace first element')
book_list[0] = 'Fight Ippo'
for i in range(0, len(book_list)):
    print(book_list[i])

print('\nTake second element')
book = book_list.pop(1)
for i in range(0, len(book_list)):
    print(book_list[i])

print('\nShow previous taken element')
print(book)

print('\nPop w/o parameter')
book_list.pop()
for i in range(0, len(book_list)):
    print(book_list[i])

print('\nPop with - sign')
book_list = ['One Piece', 'Das Capital', '1984', 'Sun Tzu']
book_list.pop(-2)
for i in range (0, len(book_list)):
    print(book_list[i])

print('\nDeleting using del')
book_list = ['One Piece', 'Das Capital', '1984', 'Sun Tzu']
del book_list[2]
for i in range(0, len(book_list)):
    print(book_list[i])

