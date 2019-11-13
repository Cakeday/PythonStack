from django.shortcuts import render, redirect
from .models import Show

def index(request):
    if request.method == 'GET':
        return redirect('/shows')

def create(request):
    if request.method == 'POST':
        Show.objects.create(title=request.POST['title'], network=request.POST['network'], release_date=request.POST['release_date'], description=request.POST['description'])
        new=Show.objects.last()
        return redirect(f'/shows/{new.id}')

def display(request, id):
    if request.method == 'GET':
        context = {
            "show_info" : Show.objects.get(id=id),
        }
        return render(request, 'TVShows/display.html', context)

def everything(request):
    if request.method == 'GET':
        context = {
            "shows" : Show.objects.all()
        }
        return render(request, 'TVShows/everything.html', context)

def edit(request, id):
    if request.method == 'GET':
        context = {
            "show_info" : Show.objects.get(id=id),
        }
        return render(request, 'TVShows/edit.html', context)

def update(request):
    if request.method == 'POST':
        show_to_update = Show.objects.get(id=request.POST['id'])
        show_to_update.title = request.POST['title']
        show_to_update.network = request.POST['network']
        show_to_update.release_date = request.POST['release_date']
        show_to_update.description = request.POST['description']
        show_to_update.save()
        return redirect(f'/shows/{show_to_update.id}')

def destroy(request, id):
    if request.method == 'POST':
        show_to_delete = Show.objects.get(id=id)
        show_to_delete.delete()
        return redirect('/shows')





# Create your views here.
