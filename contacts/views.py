from contacts.models import Contact
from gc import get_objects
from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, Http404
from django.template.defaultfilters import title
from django.views.generic import ListView
from .forms import *
from .models import *
import datetime
from django.core.paginator import Paginator
from django.views.decorators.http import require_POST
from django.utils.text import slugify
from django.db.models import Q
from django.contrib.postgres.search import SearchVector, SearchQuery, SearchRank
from django.contrib.postgres.search import TrigramSimilarity



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




def contact_search(request):
    query = None
    results = []
    if 'query' in request.GET:
        form = SearchForm(data = request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']

            result1 = Contact.published.filter(first_name__icontains=query) # az list post haye publish shode filter kon on haE ke IN query tosh hast ro
            result2 = Contact.published.filter(last_name__icontains=query)
            results = result1 | result2

            # results = Contact.published.filter(Q(title__icontains=query) | Q(description__icontains=query)) # behine shode 3 khat ghabli

            # results = Post.objects.filter(Q(title__search = query) | Q(description__search = query))

            # results = Post.objects.annotate(search = SearchVector('description', 'title', 'slug')).filter(search=query).order_by('-search') # jostojoyE ke kol server ra dargir mikone VALI search_vector mire dakhel ona peyda mikone

            # search_query = SearchQuery(query)
            # search_vector = SearchVector('last_name', weight='A')+SearchVector('first_name', weight='B') # weight yani alan ma darim bar asas ahamiat MORATAB mikonim va A emtiaz bishtar az B dare alan title kheyyyyli moheme va emtiaz balaE migire
            # results = Contact.objects.annotate(search=search_vector, rank = SearchRank(search_vector, search_query)).filter(search=search_query).order_by('-rank') # query ro peyda mikone va rank bar asas tedad query peyda shode moratab mikone

            ## baraye peyda kardan query search shode ba ajzaye mojod dar database AMMA bar asas shabahat
            # results = Contact.published.annotate(similarity=TrigramSimilarity('last_name', query)) .filter(similarity__gte=0.1).order_by('-similarity') # similarity__gte mishe shedat shabahat

        context = {'form': form, 'results': results, 'query': query}
        return render(request, 'contacts/search.html', context)

