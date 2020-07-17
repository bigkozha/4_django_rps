from django.shortcuts import render, reverse

def index(request):
    return render(request, 'index.html')