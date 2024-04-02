from django.shortcuts import render
from cisharp.models import Cisharp

# Create your views here.
def cisharp(request):
    jav = Cisharp.objects.all
    return render(request, 'cisharp.html', {'jav': jav})