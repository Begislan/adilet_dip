from django.shortcuts import render
from java.models import Java

def java(request):
    jav = Java.objects.all
    return render(request, 'java.html', {'jav': jav})

def java_detail(request, pk):
    java_detail = Java.objects.get(pk=pk)
    return render(request, 'detail/java_detail.html', {'java_detail':java_detail})