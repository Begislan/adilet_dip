from django.shortcuts import render
from .models import JavaScript

# Create your views here.
def javascript(request):
    jav = JavaScript.objects.all
    return render(request, "javascript.html", {'jav': jav})