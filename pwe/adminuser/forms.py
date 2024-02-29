from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from django.forms.models import ModelForm
from django.forms.widgets import FileInput
from .models import *


class CreateUserForm(UserCreationForm):
    class Meta:
        model =User
        fields = ['username','email','password1' ,'password2']

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'
        exclude = ['user']
        widgets ={
            'profile_img': FileInput(),
        }
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'description', 'image']  # Assuming 'title', 'content', and 'image' are fields in your Post model

        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 5}),
            'image': forms.ClearableFileInput(attrs={'class': 'form-control-file'}),
        }

