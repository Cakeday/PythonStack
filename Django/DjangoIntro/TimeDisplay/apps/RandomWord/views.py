from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string



def index(request):
    if 'counter' not in request.session:
        request.session['counter']=0
    else:
        request.session['counter']+=1
    return redirect('/generate')

def generator(request):
        request.session['generated']=get_random_string(length=14)
        print(request.session['counter'])
        request.session['counter']+=1
        return render(request, 'RandomWord/index.html')

def clear(request):
    request.session.clear()
    return redirect('/random_word')

def postroute(request):
    if request.method == 'POST':
        a = request.POST['key']
        return redirect('/wherever')
    if request.method == 'GET':
        return render(request, "test.html")


def test(request):
    return render(request, 'RandomWord/test.html')