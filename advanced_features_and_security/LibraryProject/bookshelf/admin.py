from django.contrib import admin

from advanced_features_and_security.LibraryProject.relationship_app.admin import CustomUserAdmin
from .models import Book, CustomUser
from .models import Book
# Register your models here.
class BookAdmin(admin.ModelAdmin):
    list_filter=('title','author','publication_year')
    search_fields=('title','author')
admin.site.register(Book,BookAdmin)
admin.site.register(CustomUser, CustomUserAdmin)

from django.contrib import admin
from .models import Book, CustomUser

admin.site.register(Book)
admin.site.register(CustomUser)