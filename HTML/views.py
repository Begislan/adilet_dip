from django.shortcuts import render
from .models import *

# Create your views here.
def html(request):
    jav = Html.objects.all
    return render(request, "ver.html", {'jav': jav})

def html_detail(request, pk):
    html = Html.objects.get(pk=pk)
    return render(request, "detail/html_detail.html", {'html': html})