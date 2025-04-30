from django.http import HttpResponse
from django.shortcuts import render
from .models import CallInfo
from django.contrib import messages


def index(request):
    if request.method == "POST":
        formcall = request.POST.get("formcall")
        callname = request.POST.get('callname')
        callemail = request.POST.get('callemail')
        callmessage = request.POST.get('callmessage')
        if formcall == 'CallForm':
            try:
                CallInfo.objects.create(
                    namecall = callname,
                    emailcall = callemail,
                    messagecall = callmessage,
                )
                messages.success(request, 'پیام با موفقیت ایجاد شد!')
            except Exception as e:
                messages.error(request, f'خطا در ثبت‌نام: {str(e)}')
    return render(request, 'index/index.html')

