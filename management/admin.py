from django.contrib import admin
from .models import ContactMessage

@admin.register(ContactMessage)
class ContactMessageAdmin(admin.ModelAdmin):
    list_display = ('usernamesignup', 'emailsignup', 'phonesignup', 'passwordsignup')
    search_fields = ('usernamesignup', 'emailsignup', 'phonesignup', 'passwordsignup')