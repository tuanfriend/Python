from django.shortcuts import render, redirect
from .models import Book, Authors

def index(request):
    content = {
        "all_books": Book.objects.all()
    }
    return render(request, "books_authors_app/index.html", content)

def addbook(request):
    title = request.POST["title"]
    desc = request.POST["desc"]
    Book.objects.create(title=title, desc=desc)
    return redirect('/')

def viewbook(request, id):
    ebook = Book.objects.get(id=id)
    content = {
        "ebook" : ebook,
        "vauthors" : ebook.authors.all(),
        "allauthors": Authors.objects.all()
    }
    return render(request, "books_authors_app/book_detail.html", content)

def addauth(request):
    auth_id = request.POST["auth_id"]
    ebook = Book.objects.get(id=request.POST["ebookid"])
    ebook.authors.add(Authors.objects.get(id=auth_id))
    return redirect('/books/'+str(ebook.id))

def auth_page(request):
    content = {
        "all_auths": Authors.objects.all()
    }
    return render(request, "books_authors_app/authors.html", content)

def addauthor(request):
    firstname = request.POST["fname"]
    lastname = request.POST["lname"]
    notes_form = request.POST["notes"]
    Authors.objects.create(first_name=firstname, last_name=lastname, notes=notes_form)
    return redirect('/authors')

def viewauth(request, id):
    e_auth = Authors.objects.get(id=id)
    content = {
        "e_auth" : e_auth,
        "book_auth" : e_auth.books.all(),
        "allbooks": Book.objects.all()
    }
    return render(request, "books_authors_app/auth_detail.html", content)

def add_auth_form(request):
    book_id = request.POST["book_id"]
    e_auth = Authors.objects.get(id=request.POST["idauth_form"])
    e_auth.books.add(Book.objects.get(id=book_id))
    return redirect('/authors/'+str(e_auth.id))