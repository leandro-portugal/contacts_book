from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from django.http import Http404
from .models import Contact
from django.db.models import Q, Value
from django.db.models.functions import Concat


def index(request):
    contacts = Contact.objects.order_by('-id').filter(
        show=True
    )
    paginator = Paginator(contacts, 10)
    page = request.GET.get('page')
    contacts = paginator.get_page(page)
    return render(request, 'contacts/index.html', {
        'contacts': contacts
    })


def show_contact(request, contact_id):
    contact = get_object_or_404(Contact, id=contact_id)
    if not contact.show:
        raise Http404
    return render(request, 'contacts/show_contact.html', {
        'contact': contact
    })


def search(request):
    term = request.GET.get('term')
    if term is None or not term:
        raise Http404()
    fields = Concat('first_name', Value(' '), 'last_name')

    contacts = Contact.objects.annotate(
        full_name=fields
    ).filter(
        Q(full_name__icontains=term) | Q(telephone__icontains=term)

    )

    paginator = Paginator(contacts, 10)
    page = request.GET.get('page')
    contacts = paginator.get_page(page)
    return render(request, 'contacts/search.html', {
        'contacts': contacts
    })
