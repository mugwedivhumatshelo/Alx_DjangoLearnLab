#Django Admin Setup for Book Model

*Step 1: Register the Book Model*
Modify 'bookshelf/admin.py' to include the Book model:
python
from django.contrib import admin
from .models import Book

admin.site.register(Book)


*Step 2: Customize the Admin Interface*
Implement custom configurations to display title, author, and publication year in the admin list view:

from django.contrib import admin
from .models import Book

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'publication_year')
    list_filter = ('author', 'publication_year')
    search_fields = ('title', 'author')

admin.site.register(Book, BookAdmin)

This setup enables efficient management of Book data through the Django admin interface.
