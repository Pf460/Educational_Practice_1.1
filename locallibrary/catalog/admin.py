from django.contrib import admin
from .models import Genre, Author, Book, BookInstance

class BooksInline(admin.TabularInline):
    model = Book
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death') #показ определённых полей
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')] #показ полей в форме, кортеж выравнивает поля по горизонтали\
    inlines = [BooksInline]


class BooksInstanceInline(admin.TabularInline):
    model = BookInstance
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
    inlines = [BooksInstanceInline]

@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('id', 'book', 'status', 'due_back')
    list_filter = ('status', 'due_back') #фильтрация по полям
    fieldsets = (
        (None, { #не применяет стили к полям
            'fields': ('book', 'imprint', 'id')
        }),
        ('Availability', { #делает названия полей жирным шрифтом
            'fields': ('status', 'due_back')
        }),
    )

admin.site.register(Genre)
