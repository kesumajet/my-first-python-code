book_list = ['Sebab Kita Semua Gila Sex', 'Mencari Cinta', 'Emha Ainun Najib']
print('\nshow variable book_list')
print(book_list)

print('\nProcces all with for in')
for book in book_list:
    print(book)

print('\nShow content book_list in index')
print(book_list[0])
print(book_list[2])


print('\nShow book_list with for in range')
for i in range(0, len(book_list)):
    print(book_list[i])

print('\nKembalikan nilai book_list')
book_list = ['Sebab Kita Semua Gila Sex', 'Mencari Cinta', 'Emha Ainun Najib']
print('\nAdd one book')
book_list.append('Jalur Langit')
for i in range(0, len(book_list)):
    print(book_list[i])
