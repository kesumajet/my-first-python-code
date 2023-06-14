"""
Looping with while to understand
"""
Book_count = 7
count_read = 0
print('Ibu berkata "Bacalah semua buku mu"')

Book_read_and_understand = 0
print(f'already read and understand {Book_read_and_understand}')

while count_read < Book_count * 2:
    count_read = count_read + 1
    if Book_read_and_understand == 6:
        print(f'Book Number {Book_read_and_understand + 1} No understand')
    else:
        Book_read_and_understand = Book_read_and_understand + 1
        print(f'Book number {Book_read_and_understand} read and understand')

print(f'Already read and understand {Book_read_and_understand}')
