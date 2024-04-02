from django.shortcuts import render
from .models import *

# Create your views here.
def html(request):
    jav = Html.objects.all
    return render(request, "ver.html", {'jav': jav})
