new_book = Book(title='1984', author='George Orwell', published_date='1949')
new_book.save()

Book.objects.all()
# [<Book: Book object (1)>]>

new_book.title='Nineteen Eighty-Four'
new_book.save(update_fields=['title'])

new_book.delete()
# (1, {'bookshelf.Book': 1})
Book.objects.all()
# <QuerySet []>