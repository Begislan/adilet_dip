from django import forms
from .models import Studyes

class BookForm(forms.ModelForm):
    class Meta:
        model = Studyes
        fields = '__all__'