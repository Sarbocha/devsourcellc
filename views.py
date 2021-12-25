from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from .models import Contact

def index(request):
    return render(request, "index.html")


def about(request):
    return render(request, "about.html")


def services(request):
    return render(request, "services.html")


def contact(request):
    if request.method == 'post':
        print("This is post")

    return render(request, "contact.html")
