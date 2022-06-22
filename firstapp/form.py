from django import forms
from .models import todotable

class todoform(forms.ModelForm):
 class Meta:
     model=todotable
     fields='__all__'