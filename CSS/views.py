from django.shortcuts import render
from .models import *


# Create your views here.
def css(request):
    jav = Css.objects.all
    return render(request, "css.html", {'jav': jav})


def css_detail(request, pk):
    css = Css.objects.get(pk=pk)
    return render(request, "detail/css_detail.html", {"css": css})
