from django.contrib.auth.models import User
from django.http import HttpRequest, HttpResponse, JsonResponse
from django.shortcuts import render, redirect
from django.contrib import messages
from .models import ContactMessage
from django.shortcuts import render, redirect, get_object_or_404
from contacts.models import Contact, PhoneNumber, Address
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required
from django.utils.text import slugify


userslist= []
users = User.objects.all()
for user in users:
    userslist.append(user.username)

def login(request):
    print(userslist)

    if request.method == "POST":
        form_type = request.POST.get('form_type')

        if form_type == 'login':
            username = request.POST.get('textlogin')
            password = request.POST.get('pswdlogin')
            request.session['username'] = username
            request.session['password'] = password
            return redirect('management:manage')

        elif form_type == 'signup':
            usernamesignup = request.POST.get('txtsignup')
            emailsignup = request.POST.get('emailignup')
            phonesignup = request.POST.get('numberignup')
            passwordsignup = request.POST.get('pswdignup')

            try:
                ContactMessage.objects.create(
                    usernamesignup=usernamesignup,
                    emailsignup=emailsignup,
                    phonesignup=phonesignup,
                    passwordsignup=passwordsignup,
                )
                messages.success(request, 'ثبت‌نام با موفقیت انجام شد!')
            except Exception as e:
                messages.error(request, f'خطا در ثبت‌نام: {str(e)}')

    return render(request, 'forms/login.html')


# for page's basic info
def manage(request):
    username = request.session.get('username')
    password = request.session.get('password')
    print(username, password)  # log for login
    if username in userslist:
        try:
            add_contact(request)
            contacts = Contact.published.all()
            # edit_contact1(request)
            # numberscontacts = PhoneNumber.objects.filter(id=id)
            if contacts:
                context = {'contacts': contacts}
                return render(request, 'forms/manage.html', context)
            else:
                return render(request, 'forms/manage.html')
        except:
            # return HttpResponse('noting found!!!')
            return render(request, 'management/404.html')
    else:
        messages.error(request, 'Username not found')
        return HttpResponse('Username not found!!!')


@login_required
def delete_contact(request, contact_id):
    contact = get_object_or_404(Contact, id=contact_id)
    contact.delete()
    return redirect('management:manage')


# def edit_contact1(request):
#     contacts1 = Contact.published.all()
#     for contact in contacts1:
#         context1 = {'contact': contact}
#         return render(request, 'forms/manage.html', context1)

def edit_contact(request, contact_id):
    contact = get_object_or_404(Contact, id=contact_id)
    if request.method == "POST":
        print("log2")
        form_type = request.POST.get('form_type')
        print("log3")
        print("log4")
        first_name_manage_edit = request.POST.get('first_name_manage')
        print("log5")
        last_name_manage_edit = request.POST.get('last_name_manage')
        print("log6")
        phone1_manage_edit = request.POST.get('phone1_manage')
        print("log7")
        email1_manage_edit = request.POST.get('email1_manage')
        print("log8")
        address1_manage_edit = request.POST.get('address1_manage')
        print("log9")
        print("log10")
        image_manage_edit = request.FILES.get('image_manage')  # فایل از request.FILES میاد
        print("log10")

        contact.first_name = first_name_manage_edit
        contact.last_name = last_name_manage_edit
        contact.email = email1_manage_edit
        contact.pic =image_manage_edit
        contact.save()

        phone_obj = contact.phone_numbers.first()
        if phone_obj:
            phone_obj.number = phone1_manage_edit
            phone_obj.save()
        else:
            PhoneNumber.objects.create(contact=contact, number=phone1_manage_edit)

        address_obj = contact.addresses.first()
        if address_obj:
            address_obj.address = address1_manage_edit
            address_obj.save()
        else:
            Address.objects.create(contact=contact, address=address1_manage_edit)

        messages.success(request, 'contact updated successfully')
        return redirect('management:manage')

    context = {'contact': contact, 'edit_mode': True}
    return render(request, 'forms/manage.html', context)




def add_contact(request):
    # print("log1")
    if request.method == "POST":
        # print("log2")
        form_type = request.POST.get('form_type')
        # print("log3")
        # print("log4")
        first_name_manage = request.POST.get('first_name_manage')
        # print("log5")
        last_name_manage = request.POST.get('last_name_manage')
        # print("log6")
        phone1_manage = request.POST.get('phone1_manage')
        # print("log7")
        email1_manage = request.POST.get('email1_manage')
        # print("log8")
        address1_manage = request.POST.get('address1_manage')
        print("log9")
        address2_manage = request.POST.get('address2_manage')
        print("log10")
        image_manage = request.FILES.get('image_manage')  # فایل از request.FILES میاد
        print("log10")


        try:
            # ساخت Contact
            contact = Contact.objects.create(
                first_name=first_name_manage,
                last_name=last_name_manage,
                email=email1_manage,
                pic=image_manage,
                slug=slugify(f"{first_name_manage}-{last_name_manage}"),  # slug منحصربه‌فرد
                author=request.user,
                status='published'
            )
            print("log11")

            # ساخت PhoneNumber
            if phone1_manage:
                PhoneNumber.objects.create(
                    contact=contact,
                    number=phone1_manage
                )
            print("log12")
            # ساخت Address
            if address1_manage:
                Address.objects.create(
                    contact=contact,
                    address=address1_manage
                )
            print("log14")
            if address2_manage:  # آدرس دوم اگه وجود داره
                Address.objects.create(
                    contact=contact,
                    address=address2_manage
                )

            messages.success(request, 'مخاطب با موفقیت اضافه شد!')
            return redirect('management:manage')  # برگشت به لیست مخاطبین


        except Exception as e:
            messages.error(request, f'خطا در ثبت مخاطب: {str(e)}')
            return render(request, 'forms/manage.html')  # برگشت به فرم با خطا
            # return HttpResponse('Username not found!!!')

#    اگه GET باشه، فرم خالی نشون بده
    return render(request, 'forms/manage.html')





