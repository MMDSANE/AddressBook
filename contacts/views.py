from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404

from contacts.models import Contact


def contacts_list(request):
    try:
        contactslist = Contact.published.all()
        if contactslist:
            context = {'contactslist': contactslist}
            return render(request, 'contacts/contacts-list.html', context)
        else:
            context = {'contactslist': []}
            return render(request, 'contacts/contacts-list.html', context)
    except:
        # return render(request, 'contacts/404.html')
        return HttpResponse('Something went wrong')

def single_contact(request, id):
    contact_single = get_object_or_404(Contact, id=id)
    contextsinlecontact = {'contact_single': contact_single}
    return render(request, 'contacts/single-contact.html', contextsinlecontact)

    # try:
    #     contact_single = Contact.published.get(id=id)
    #     if contact_single:
    #         contextsinlecontact = {'contact_single': contact_single}
    #         return render(request, 'contacts/single-contact.html', contextsinlecontact)
    #     else:
    #         return render(request, 'contacts/404.html')
    # except:
    #     return HttpResponse('Something went wrong2')



