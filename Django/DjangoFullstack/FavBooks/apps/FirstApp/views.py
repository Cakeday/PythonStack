from django.shortcuts import render, redirect
from .models import User, Book
from django.contrib import messages
import bcrypt

def index(request):
    return render(request, 'FirstApp/index.html')

def register(request):
    if request.method == 'POST':
        errors = User.objects.registration_validator(request.POST)
        if len(errors) > 0:
            for key, value in errors.items():
                messages.error(request, value, extra_tags=key)
            return redirect('/')
        pw = request.POST['password']
        hash = bcrypt.hashpw(pw.encode(), bcrypt.gensalt())
        x = User.objects.create(first_name=request.POST['first_name'], last_name=request.POST['last_name'], email=request.POST['email'], hashpw=hash)
        request.session['userid_in_session'] = x.id
        return redirect('/welcome')

def welcome(request):
    if 'userid_in_session' in request.session:
        user = User.objects.get(id=(request.session['userid_in_session']))
        context = {
            'user': user,
            'all_books' : Book.objects.all(),
        }
        return render(request,'FirstApp/welcome.html', context)
    else:
        print('redirecting?????????????????????????????')
        return redirect('/')

def login(request):
    if request.method == 'POST':
        errors = {}
        user = User.objects.filter(email=request.POST['email'])
        if user:
            logged_user = user[0]
            if bcrypt.checkpw(request.POST['password'].encode(), logged_user.hashpw.encode()):
                request.session['userid_in_session'] = logged_user.id
                print('OK I ACTUALLY MADE IT IN LOL SCKGHJVSCKJYGVSCKHGVSCKHGSVCXKHGSVCMHGVSCMHGSVCHKMSCVH')
                return redirect('/welcome')
            else:
                messages.error(request, "Incorrect password")
                return redirect('/')
        else:
            messages.error(request, "User doesn't exist")
            return redirect('/')

def logout(request):
    if request.method == 'GET':
        request.session.clear()
        return redirect('/')

def add_a_book(request):
    if request.method == 'POST':
        errors = Book.objects.book_validator(request.POST)
        if len(errors)>0:
            for key, value in errors.items():
                messages.error(request, value)
            return redirect('/welcome')
        user = User.objects.get(id=request.session['userid_in_session'])
        new_book = Book.objects.create(title=request.POST['title'], description=request.POST['description'], uploaded_by=user)
        user.liked_books.add(new_book)
        return redirect(f'books/{new_book.id}')

def book_parser(request, id):
    if 'userid_in_session' in request.session:
        if request.method == 'GET':
            user = User.objects.get(id=(request.session['userid_in_session']))
            the_book = Book.objects.get(id=id)
            context = {
                'user': user,
                'all_books' : Book.objects.all(),
                'the_book' : Book.objects.get(id=id),
                'all_users' : User.objects.all(),
                'users_who_like' : Book.objects.get(id=id).users_who_like.all(),
            }
            the_user_id = request.session['userid_in_session']
            if the_user_id == the_book.uploaded_by_id:
                return render(request, 'FirstApp/book_edit.html', context)
            else:
                # print(context[''])
                return render(request, 'FirstApp/book_display.html', context)
    else:
        print("redirecting because I'm not in session?????????????????????????????")
        return redirect('/')

def book_update(request, id):
    context = {
        "book" : Book.objects.get(id=id)
    }
    print('did i make it here???????????????????????????????????????????????????????????')
    return render(request, 'FirstApp/book_edit.html', context)

def favorite(request, id):
    the_book = Book.objects.get(id=id)
    user_id = request.session['userid_in_session']
    the_user = User.objects.get(id=user_id)
    the_user.liked_books.add(the_book)
    return redirect(f'/books/{id}')