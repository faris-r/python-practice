print('\nDeleting using del with list comprehension')
book_list = ['One Piece', 'Das Capital', '1984', 'Sun Tzu']
del book_list[:]
for i in range(0, len(book_list)):
    print(book_list[i])

print('\nDeleting using del with list comprehension -start')
book_list = ['One Piece', 'Das Capital', '1984', 'Sun Tzu']
del book_list[0:2]
for i in range (0, len(book_list)):
    print(book_list[i])

print('\nDeleting using del with list comprehension end-')
book_list = ['One Piece', 'Das Capital', '1984', 'Sun Tzu']
del book_list[0:-3]
for i in range(0, len(book_list)):
    print((book_list[i]))

print('\nDeleting using del with list comprehension step')
book_list = ['One Piece', 'Das Capital', '1984', 'Sun Tzu', 'Tan']
del book_list[1::2]
for i in range(0, len(book_list)):
    print(book_list[i])

print('\nMaking a New List')
book_list = ['One Piece', 'Das Capital', '1984', 'Sun Tzu', 'Tan']
book_list_new = book_list[:]
del book_list[0:3]
for i in range(0, len(book_list_new)):
    print(book_list_new[i])
print(book_list[0])

print('\nMaking a New List: odd')
book_list = ['One Piece', 'Das Capital', '1984', 'Sun Tzu', 'Tan']
book_list_new = book_list[0::2]
del book_list[:]
for i in range(0, len(book_list_new)):
    print(book_list_new[i])

print('\nMaking a New List: even')
book_list = ['One Piece', 'Das Capital', '1984', 'Sun Tzu', 'Tan']
book_list_new = book_list[1::2]
del book_list[:]
for i in range(0, len(book_list_new)):
    print(book_list_new[i])

print('\nMaking a New List: -, odd elements')
book_list = ['One Piece', 'Das Capital', '1984', 'Sun Tzu', 'Tan']
book_list_new = book_list[0:-1:2]
del book_list[:]
for i in range(0, len(book_list_new)):
    print(book_list_new[i])