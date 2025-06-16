from django import forms
from django.core.exceptions import ValidationError

from .models import Notes

class NotesForm(forms.ModelForm):
    class Meta:
        model = Notes
        fields = ('title', 'text', 'public')
        
    def clean_title(self):
        title = self.cleaned_data['title']
        return title