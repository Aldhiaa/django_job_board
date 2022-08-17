from dataclasses import fields
from pyexpat import model
from django import forms
from .models import Apply,job

class Applyform(forms.ModelForm):
    class Meta:
        model=Apply
        fields = ['name','email','website','CV','cover_letter']

class JobForm(forms.ModelForm):
    class Meta:
        model = job
        fields = '__all__'
        exclude = ('owner','slug')