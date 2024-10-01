from django.shortcuts import render
from .paginator import paginator

from .models import Item


def product(request):
    return render (request, 'main.html')


def contacts(request):
    return render (request, 'contacts.html')


def catalog(request):
    return render(request, 'catalog.html')


def login(request):
    return render (request, 'account/login.html')


def logout(request):
    return render(request, 'account/logout.html')


def signup(request):
    return render(request, 'account/signup.html')


def store(request):
    items = Item.objects.filter(is_available=True)
    context = {
        'page_obj': paginator(request, items, 9),
        'range': [*range(1, 7)],  # For random css styles
    }

    return render(request, 'catalog.html', context)
