from django.shortcuts import render, redirect , get_object_or_404
from .models import Author,Book , Genre
from .forms import Authorform , Booksform , Genreform

def addauthor(request):
    if request.method == "POST":
        form = Authorform(request.POST)
        if form.is_valid():
            form.save()
            return redirect ('addauthor')        
    else:
        form = Authorform()
    return render (request,"library/addauthor.html",{"form":form})

def addbooks(request):
    if request.method == "POST":
        form = Booksform(request.POST)
        if form.is_valid():
            form.save()
            return redirect('addbooks')
    else:
        form = Booksform()
    return render (request,"library/addbooks.html",{"form":form})


def author(request):
    authors = Author.objects.all()
    return render (request,"library/author.html",{"authors":authors})

def books(request):
    books = Book.objects.select_related("author").all()
    return render (request,"library/books.html",{"books":books})

def deleteAuthor(request,pk):
    author = get_object_or_404(Author, pk = pk)
    author.delete()
    return redirect ('author')

def deleteBook(request,pk):
    book = get_object_or_404(Book, pk = pk)
    book.delete()
    return redirect ('books')

def addgenre(request):
    if request.method == "POST":
        form = Genreform(request.POST)
        if form.is_valid():
            form.save()
            return redirect ("addgenre")
    else:
        form = Genreform()
    return render (request,"library/addgenre.html",{"form":form})


def genre(request):
    genre = Genre.objects.all()
    return render (request,"library/genre.html",{"genre":genre})


def home(request):
    return render (request,'library/home.html')

def update(request, pk):
    book = get_object_or_404(Book, pk =pk)
    if request.method =="POST":
        form = Booksform(request.POST, instance = book)
        if form.is_valid():
            form.save()
            return redirect ('books')
    else:
        form = Booksform(instance = book)
    return render (request, "library/updatebooks.html",{'form':form})

