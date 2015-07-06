from django.contrib import admin
from books.models import Publisher, Author, Book

class AuthAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email')
    search_fields = ('first_name', 'last_name')

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'publisher', 'publisher_date')
    list_filter = ('publisher_date',)
    date_hierarchy = 'publisher_date'

admin.site.register(Author, AuthAdmin)
admin.site.register(Publisher)
admin.site.register(Book, BookAdmin)
