from django.shortcuts import render
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from .models import Studyes
from django.urls import reverse_lazy
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
data = Studyes.objects.all()

def study_list(request):
    return render(request, 'study/list_study.html', {'data': data})

def study_detail(request, pk):
    data_detail = Studyes.objects.get(id=pk)
    return render(request, 'study/detail_study.html', locals())


class CreateStudy(CreateView):
    model = Studyes
    template_name = 'study/create_list.html'
    fields = '__all__'

    def get_success_url(self):
        # Use the primary key of the updated object to generate the success URL
        return reverse_lazy('study_detail', kwargs={'pk': self.object.pk})

class UpdateStudy(UpdateView):
    model = Studyes
    fields = '__all__'  # Fields to be updated
    template_name = 'study/upfate_study.html'
    def get_success_url(self):
        # Use the primary key of the updated object to generate the success URL
        return reverse_lazy('study_detail', kwargs={'pk': self.object.pk})


def DeleteStudyView(request, pk):
    data_d = get_object_or_404(Studyes, pk=pk)

    if request.method == 'POST':
        data_d.delete()
        return redirect('study_list')
    return render(request, 'study/delete_study.html', locals())