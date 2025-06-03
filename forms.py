from django import forms
from testapp.models import BlogModel
from django.contrib.auth.models import User
class BlogForm(forms.ModelForm):
    class Meta:
        model=BlogModel
        fields=['title','content','image']
class SignUpForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['first_name','last_name','username','password']