from django.shortcuts import render, HttpResponse
from time import gmtime, strftime

def index(request):
    context = {
        "calendar" : strftime("%b %d, %Y", gmtime()),
        "hour" : strftime("%I:%M %p", gmtime())
    }
    return render(request, 'CurrentTime/index.html', context)

# Create your views here.
