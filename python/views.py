from django.shortcuts import render
from core.models import Python

def pyt(request):
    lays = Python.objects.all
    return render(request, "python.html", {'lays': lays})