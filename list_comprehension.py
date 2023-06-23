print('\nPerintah del')
book_list = ['Sebab Kita Semua Gila Sex', 'Mencari Cinta', 'Emha Ainun Najib']
del book_list[0]
for i in range(0, len(book_list)):
    print(book_list[i])

print('\nPerintah del with command comprehension')
book_list = ['Sebab Kita Semua Gila Sex', 'Mencari Cinta', 'Emha Ainun Najib']
del book_list[:]
for i in range(0, len(book_list)):
    print(book_list[i])

print('\nPerintah del with command comprehension start stop')
book_list = ['Sebab Kita Semua Gila Sex', 'Mencari Cinta', 'Emha Ainun Najib']
del book_list[0:1]
#index dimulai dari 0 dan jumlah dari 1
#depan adalah index
#belakang adalah jumlah
#juga bisa dari belakang dengan (-)
for i in range(0, len(book_list)):
    print(book_list[i])

print('\nPerintah del with command comprehension start stop step')
book_list = ['Sebab Kita Semua Gila Sex', 'Mencari Cinta', 'Emha Ainun Najib']
del book_list[0::2]
for i in range(0, len(book_list)):
    print(book_list[i])

print('\nCreate new list')
book_list = ['Sebab Kita Semua Gila Sex', 'Mencari Cinta', 'Emha Ainun Najib']
new_list_book = book_list[:]
for i in range(0, len(book_list)):
    print(book_list[i])

print('\nCreate new list')
del book_list[:]
for i in range(0, len(new_list_book)):
    print(new_list_book[i])

print('\nCreate new list')
book_list = ['Sebab Kita Semua Gila Sex', 'Mencari Cinta', 'Emha Ainun Najib']
new_list_book = book_list[:]
for i in range(0, len(book_list)):
    print(book_list[i])

print('\nCreate new list')
del book_list[:]
for i in range(0, len(new_list_book)):
    print(new_list_book[i])