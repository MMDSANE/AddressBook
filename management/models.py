from django.db import models

class ContactMessage(models.Model):
    usernamesignup = models.CharField(max_length=255, verbose_name="نام کاربری")
    emailsignup = models.EmailField(verbose_name="ایمیل")
    phonesignup = models.CharField(max_length=11, verbose_name="شماره تلفن")
    passwordsignup = models.CharField(max_length=255, verbose_name="پسورد")

    class Meta:
        verbose_name = "SIGN UP"
        verbose_name_plural = "SING UP"

    def __str__(self):
        return f"{self.usernamesignup} - {self.passwordsignup}"
