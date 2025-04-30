from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django_jalali.db import models as jmodels
from django.urls import reverse

class PublishedManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(status='published')  # مقدار صحیح برای فیلتر

class Contact(models.Model):
    STATUS_CHOICES = (
        ('draft', 'Draft'),
        ('published', 'Published'),
    )

    first_name = models.CharField(max_length=50, verbose_name='نام')
    last_name = models.CharField(max_length=50, verbose_name='نام خانوادگی')
    email = models.EmailField(max_length=150, verbose_name='ایمیل', unique=True)
    pic = models.FileField(upload_to='pics/pictures', null=True, blank=True, default='pics/pictures/low-qlt-thumb.jpg' ,verbose_name='عکس مخاطب')
    slug = models.SlugField(max_length=250, unique=True)
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='published', verbose_name='وضعیت')

    # تاریخ ایجاد
    create_at = jmodels.jDateTimeField(default=timezone.now)

    class Meta:
        ordering = ['-create_at']
        indexes = [models.Index(fields=['slug'])]
        verbose_name = 'مخاطب'
        verbose_name_plural = 'مخاطبین'

    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name='contacts', verbose_name='نویسنده', default=1)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

    objects = models.Manager()  # مدیر پیش‌فرض
    published = PublishedManager()  # مدیر برای داده‌های منتشر شده

    def get_absolute_url_delete(self):
        return reverse('management:delete_contact', args=[self.id])


    def get_absolute_url_edit(self):
        return reverse('management:edit_contact', args=[self.id])

    def get_absolute_url(self):
        return reverse('contacts:single_contact', args=[self.id])

class PhoneNumber(models.Model):
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE, related_name='phone_numbers')
    number = models.CharField(max_length=15, unique=True)

    def __str__(self):
        return self.number

class Address(models.Model):
    contact = models.ForeignKey(Contact, on_delete=models.CASCADE, related_name='addresses')
    address = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.address if self.address else "بدون آدرس"



