"""
Looping with python
"""
Book_count = 7
print('Ibu berkata "Bacalah semua buku mu"')

Book_read_count = 0
print(f'already read {Book_read_count}')

for Book_read_count in range(1, Book_count+1):
    print(f'Book number {Book_read_count} done read')

print(f'book already read {Book_read_count}')
