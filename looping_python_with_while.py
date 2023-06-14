"""
Looping with while
"""
Book_count = 7
print('Ibu berkata "Bacalah semua buku mu"')

Book_read_count = 0
print(f'already read {Book_read_count}')

while Book_read_count < Book_count:
    Book_read_count = Book_read_count + 1
    print(f'Book number {Book_read_count} already read')

print(f'Already read {Book_read_count}')
