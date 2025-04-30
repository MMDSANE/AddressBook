from django.db import models

class CallInfo(models.Model):
    namecall = models.CharField(max_length=255, verbose_name="نام")
    emailcall = models.EmailField(verbose_name="ایمیل")
    messagecall = models.TextField(verbose_name="پیام")
    createdcall_at = models.DateTimeField(auto_now_add=True, verbose_name="تاریخ ارسال")


    class Meta:
        verbose_name = "CALLS"
        verbose_name_plural = "CALLS"

    def __str__(self):
        return f"{self.namecall} - {self.emailcall}"
