from django.shortcuts import render, redirect
from .models import User
from django.contrib import messages
import bcrypt

def index(request):
    return render(request, 'Loopy/index.html')

def beat(request):
    if 'userid_in_session' in request.session:
        user = User.objects.get(id=(request.session['userid_in_session']))
        context = {
            'user': user
        }
        return render(request,'Loopy/clip.html', context)
    else:
        return redirect('/')

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
        return redirect('/beat')


def login(request):
    if request.method == 'POST':
        errors = {}
        user = User.objects.filter(email=request.POST['email'])
        if user:
            logged_user = user[0]
            if bcrypt.checkpw(request.POST['password'].encode(), logged_user.hashpw.encode()):
                request.session['userid_in_session'] = logged_user.id
                return redirect('/beat')
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