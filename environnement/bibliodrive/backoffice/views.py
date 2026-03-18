from django.shortcuts import render, HttpResponse, redirect
from .models import Author, Title, Publishers
from django.db.models import Q
from .form import signup
from django.contrib.auth import authenticate, login, logout


# Create your views here.

def home(request, nom="Test"):
    html = f"<html><body>TRY {nom}</body></html>"
    return HttpResponse(html)

def acceuil(request, nom="Acceuil"):
    return render(request, 'acceuil.html', {'active_nav': 'acceuil'})

def about(request, nom="A Propos de"):
    html = f"<html><body>TRY {nom}</body></html>"
    return HttpResponse(html)

def author(request):
    author = Author.objects.all()
    return render(request, 'author/author.html', {'author': author, 'active_nav': 'author'})

def author_detail(request, author_id):
    author = Author.objects.get(id = author_id)
    books = Title.objects.filter(authors = author_id)
    return render(request, 'author/author_detail.html', {'author': author, 'books': books, 'active_nav': 'author'})

def book(request):
    querry = request.GET.get("querryTitle", "")
    if (querry):
        book = Title.objects.filter(Q(title__icontains=querry) | Q(isbn__icontains=querry) | Q(subject__icontains=querry))
    else:
        book = Title.objects.all()
    return render(request, 'book/book.html', {'book': book, 'querry': querry, 'active_nav': 'book'})

def book_detail(request, book_id):
    book = Title.objects.get(pk = book_id)
    pub = Publishers.objects.filter(pk=book.pubid.pk)
    return render(request, 'book/book_detail.html', {'book': book, 'pub': pub,  'active_nav': 'book'})

def publisher(request):
    publisher = Publishers.objects.all()
    return render(request, 'publisher/publisher.html', {'publisher': publisher, 'active_nav': 'publisher'})

def publisher_detail(request, pubid):
    publisher = Publishers.objects.get(pk = pubid)
    book = Title.objects.filter(pubid = pubid)
    return render(request, 'publisher/publisher_detail.html', {'pub': publisher, 'book': book, 'active_nav': 'publisher'})

def signup_view(request):
    if request.method == "POST":
        form = signup(request.POST)
        if form.is_valid :
            user = form.save()
            return redirect('acceuil')
    else :
        form = signup()
    return render(request, 'signup.html', {'form': form})

def login_view(request):
    if request.method =="POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if (user is not None):
            login(request, user)
            return redirect("acceuil")
    return render(request, 'login.html')

def logout_view(request):
    logout(request)
    return redirect("acceuil")

def book_reserved(request, book_id):
    book = Title.objects.get(pk = book_id)
    book.reserved = not book.reserved
    book.save()
    return redirect("acceuil")