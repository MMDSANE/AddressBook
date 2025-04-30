from django.contrib import admin
from .models import CallInfo

@admin.register(CallInfo)
class CallInfoAdmin(admin.ModelAdmin):
    list_display = ('namecall', 'emailcall', 'messagecall', 'createdcall_at')
    search_fields = ('namecall', 'emailcall', 'messagecall', 'createdcall_at')
    list_filter = ('createdcall_at',)
