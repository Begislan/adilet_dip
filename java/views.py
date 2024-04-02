from django.shortcuts import render
from java.models import Java

def java(request):
    jav = Java.objects.all
    return render(request, 'java.html', {'jav': jav})
