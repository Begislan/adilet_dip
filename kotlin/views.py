from django.shortcuts import render
from .models import *

# Create your views here.
def kotlin(request):
    jav = Kotlin.objects.all
    return render(request, "kotlin.html", {'jav': jav})
