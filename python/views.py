from django.shortcuts import render
from core.models import Python

def pyt(request):
    lays = Python.objects.all
    return render(request, "python.html", {'lays': lays})

def detail_python(request, pk):
    lay = Python.objects.get(pk=pk)
    return render(request, "detail/py_detail.html", {'lay': lay})