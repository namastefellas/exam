from django.contrib import admin
from webapp.models import GuestBook

# Register your models here.

class GuestAdmin(admin.ModelAdmin):
    list_display = ['id', 'user_name', 'user_email', 'user_text', 'date_start', 'date_edit', 'status']
    fields = ['id', 'user_name', 'user_email', 'user_text', 'status']
    readonly_fields = ['id']

admin.site.register(GuestBook, GuestAdmin)