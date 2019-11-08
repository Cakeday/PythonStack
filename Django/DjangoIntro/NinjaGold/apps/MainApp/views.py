from django.shortcuts import render, redirect
import random
from time import gmtime, strftime

def index(request):
    # if 'scrollset' in request.session:
    return render(request, 'MainApp/index.html')

def process_money(request):
    if request.method == "POST":
        if 'total_gold' not in request.session:
            request.session['total_gold']=0
        if 'just_earned' not in request.session:
            request.session['just_earned']=0

        if request.POST['some_action']=='farm':
            request.session['type'] = request.POST['some_action']
            request.session['just_earned']=random.randint(10,20)
            request.session['total_gold']+=int(request.session['just_earned'])
            return redirect('/scroll_bar')

        if request.POST['some_action']=='cave':
            request.session['type'] = request.POST['some_action']
            request.session['just_earned']=random.randint(5,10)
            request.session['total_gold']+=int(request.session['just_earned'])
            return redirect('/scroll_bar')

        if request.POST['some_action']=='house':
            request.session['type'] = request.POST['some_action']
            request.session['just_earned']=random.randint(2,5)
            request.session['total_gold']+=int(request.session['just_earned'])
            return redirect('/scroll_bar')

        if request.POST['some_action']=='casino':
            request.session['type'] = request.POST['some_action']
            request.session['just_earned']=random.randint(-50,50)
            request.session['total_gold']+=int(request.session['just_earned'])
            return redirect('/scroll_bar')

    if request.method == "GET":
        pass
    return render(request, 'MainApp/index.html')

def scroll_bar(request):
    
    request.session.modified = True
    if 'scrollset' not in request.session:
        request.session['scrollset']=[]
    if request.session['just_earned']>0:
        time = strftime('%b %d, %Y, %I:%M %p', gmtime())
        request.session['scrollset'].insert(0,f"Earned {request.session['just_earned']} gold from the {request.session['type']}! {time}")
        return redirect('/')
    if request.session['just_earned']<=0:
        time = strftime('%b %d, %Y, %I:%M %p', gmtime())
        request.session['scrollset'].insert(0,f"Entered a casino and lost {request.session['just_earned']} gold... Ouch.. {time}")
        return redirect('/')




