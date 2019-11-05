from django.shortcuts import render, HttpResponse

def index(request):
    return render(request, 'CurrentTime/index.html')

# Create your views here.
