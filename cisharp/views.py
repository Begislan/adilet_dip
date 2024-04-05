from django.shortcuts import render
from cisharp.models import Cisharp

# Create your views here.
def cisharp(request):
    jav = Cisharp.objects.all
    return render(request, 'cisharp.html', {'jav': jav})

def cisharp_detail(request, pk):
    jav_det = Cisharp.objects.get(pk=pk)
    return render(request, 'detail/cisharp_detail.html', {'jav_det': jav_det})