from django.shortcuts import render
from .models import *

# Create your views here.
def kotlin(request):
    jav = Kotlin.objects.all
    return render(request, "kotlin.html", {'jav': jav})

def kotlin_detail(request, pk):
    kotlin = Kotlin.objects.get(pk=pk)
    return render(request, "detail/kotlin_detail.html", {'kotlin':kotlin})