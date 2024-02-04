from django import forms
from .models import Member


class MyModelForm(forms.ModelForm):
    class Meta:
        model = Member
        fields = ['description']