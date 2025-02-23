Book.objects.filter(author="name")
Library.objects.get(name=library_name)
Library.objects.get(books.all())
Librarian.objects.get(Library="library")