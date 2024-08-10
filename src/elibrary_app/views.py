from django.shortcuts import render
from django.http import HttpResponse

from elibrary_app.forms import AddBookForm
from elibrary_app.models import Catalog
from .services import get_joke


def home(request):
    if request.method == 'POST':
        add_book_form = AddBookForm(data=request.POST)
        if add_book_form.is_valid():
            add_book_form.save()
    chuk_say = get_joke()
    print()
    print(f"--chuk_say {chuk_say}")
    print()
    books = Catalog.objects.all()
    add_book_form = AddBookForm()
    return render(request, 'elibrary_app/home.html', {
        "add_book_form": add_book_form,
        "books": books,
        "chuck_say": chuk_say
    })
