from django.contrib import admin
from .models import Category, Contact


class ContactAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'telephone', 'email', 'creation_date', 'category', 'show')
    list_display_links = ('first_name', 'last_name')
    list_per_page = 15
    search_fields = ('first_name', 'last_name', 'telephone')
    list_editable = ('telephone', 'show')


admin.site.register(Category)
admin.site.register(Contact, ContactAdmin)
