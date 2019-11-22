from django.shortcuts import render, redirect

def index(request):
    return render(request, 'Loopy/index.html')

def beat(request):
    return render(request, 'Loopy/clip.html')

