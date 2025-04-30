from django.contrib import admin
from .models import *
from django_jalali.admin.filters import JDateFieldListFilter
import django_jalali.admin as jadmin

# Register your models here.

admin.sites.AdminSite.site_header = 'پنل مدیریت جنگو'
admin.sites.AdminSite.site_title = 'پنل مدیریت'
admin.sites.AdminSite.index_title = 'پنل ادمین اپلیکیشن مخاطبین'


class PhoneNumberInline(admin.TabularInline):  # یا از admin.StackedInline استفاده کن
    model = PhoneNumber
    extra = 1  # تعداد فیلدهای خالی برای اضافه کردن شماره‌های جدید

class AddressInline(admin.TabularInline):
    model = Address
    extra = 1  # تعداد فیلدهای خالی برای اضافه کردن آدرس‌های جدید

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['first_name', 'last_name', 'email']
    ordering = ('last_name','-create_at')
    list_filter = ('first_name', 'last_name', 'email', ('create_at', JDateFieldListFilter))
    search_fields = ('first_name', 'last_name', 'email')
    date_hierarchy = 'create_at'
    raw_id_fields = ('author',)
    prepopulated_fields = {'slug': ('last_name',)}
    # list_editable = ('status',)
    list_display_links = ('last_name', 'email')
    inlines = [PhoneNumberInline, AddressInline]  # اضافه کردن شماره و آدرس به فرم مخاطب

