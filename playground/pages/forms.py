from django import forms
from .models import Page

class PageForm(forms.ModelForm):

    class Meta:
        model = Page
        fields = ['title', 'content', 'order']
        widgets = {
            'title': forms.TextInput(attrs={'class':'forms-control', 'placeholder':'Titulo'}),
            'content': forms.Textarea(attrs={'class': 'forms-control','placeholder':'Contenido'}), 
            'order' : forms.NumberInput(attrs={'class': 'forms-control'}),
        }    
        labels = {
            'title': '', 'content': '', 'order': ''
        }