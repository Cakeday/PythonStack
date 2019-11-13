from django.shortcuts import render, redirect, HttpResponse
from .models import Book, Author

def index(request):
    context = {
        "all_books":Book.objects.all()
    }
    return render(request, 'BooksAuthorsApp/index.html', context)

def books(request, id):
    this_book = Book.objects.get(id=id)
    # this_author = Author.objects.hmmmmmmmmm
    # this_book.authors.all()
    context = {
        "the_book":Book.objects.get(id=id),
        "all_books":Book.objects.all(),
        "many_authors":this_book.authors.all(),
    }
    idList = []
    for author in context['many_authors']:
        idList.append(author.id)
    context['non_authors'] = Author.objects.exclude(id__in=idList)
    return render(request, 'BooksAuthorsApp/BookDisplay.html', context)




def author_index(request):
    context = {
        "all_authors":Author.objects.all()
    }
    return render(request, 'BooksAuthorsApp/AuthorIndex.html', context)

def authors(request, id):
    this_author = Author.objects.get(id=id)
    context = {
        "the_author":Author.objects.get(id=id),
        "all_authors":Author.objects.all(),
        "many_books":this_author.books.all(),
    }
    idList = []
    for book in context['many_books']:
        idList.append(book.id)
    context['non_books'] = Book.objects.exclude(id__in=idList)
    return render(request, 'BooksAuthorsApp/AuthorDisplay.html', context)





def book_add(request):
    if request.method == "POST":
        book_to_add = Book.objects.create(title=request.POST['book_title'], desc=request.POST['book_desc'])
    return redirect('/')

def author_add(request):
    if request.method == "POST":
        author_to_add = Author.objects.create(first_name=request.POST['authf'], last_name=request.POST['authl'], notes=request.POST['authn'])
    return redirect('/authors')




def author_add_from_book(request):
    print(id)
    if request.method == "POST":
        author=Author.objects.get(id=request.POST['author_id'])
        book=Book.objects.get(id=request.POST['book_id'])
        book.authors.add(author)
    return redirect(f'/books/{book.id}')

def book_add_from_author(request):
    if request.method == "POST":
        author=Author.objects.get(id=request.POST['author_id'])
        book=Book.objects.get(id=request.POST['book_id'])
        author.books.add(book)
    return redirect(f'/authors/{author.id}')

# Create your views here.
