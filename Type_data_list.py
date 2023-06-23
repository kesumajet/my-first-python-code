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

print('\nClear List')
book_list.clear()
for i in range(0, len(book_list)):
    print(book_list[i])

print('\nGanti Element')
book_list = ['Sebab Kita Semua Gila Sex', 'Mencari Cinta', 'Emha Ainun Najib']
book_list[0] = 'eight hubby'
for i in range(0, len(book_list)):
    print(book_list[i])

print('\nAmbil Element ke - 2')
book = book_list.pop(1)
for i in range(0, len(book_list)):
    print(book_list[i])

print('\nBuku yang diambil tadi')
print(book)
#.pop adalah mengambil dari list dan menyimpan dalam variabel
#perintah pop juga dapat dipanggil tanpa parameter

book_list = ['Sebab Kita Semua Gila Sex', 'Mencari Cinta', 'Emha Ainun Najib']
print('\nPop')
book_list.pop()
for i in range(0, len(book_list)):
    print(book_list[i])

book_list = ['Sebab Kita Semua Gila Sex', 'Mencari Cinta', 'Emha Ainun Najib']
print('\nPop -1')
book_list.pop(-1)
for i in range(0, len(book_list)):
    print(book_list[i])

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
