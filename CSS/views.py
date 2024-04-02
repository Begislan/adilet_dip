from django.shortcuts import render
from .models import *

# Create your views here.
def css(request):
    jav = Css.objects.all
    return render(request, "css.html", {'jav': jav})
