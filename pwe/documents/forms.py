from django import forms
from .models import PANCard

class PANCardForm(forms.ModelForm):
    class Meta:
        model = PANCard
        fields = ['image']