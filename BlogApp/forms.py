from django.contrib.auth.forms import UserCreationForm
from django import forms

class ContactForm(forms.Form):
    emailName = forms.CharField(required=True,widget=forms.TextInput(attrs={'class': 'form-control' , "placeholder": 'Name','id':'con-name'}))
    emailSubject = forms.CharField(required=True,widget=forms.TextInput(attrs={'class': 'form-control' , "placeholder": 'Subject','id':'con-subject'}))
    email = forms.EmailField(required=True,widget=forms.TextInput(attrs={'class': 'form-control' , "placeholder": 'Email','id':'con-email'}))
    emailMessage = forms.CharField(required=True,widget=forms.Textarea(attrs={'class': 'form-control' , "placeholder": 'Message','id':'con-message',"rows":5, "cols":30}))

class LogInForm(forms.Form):
    email = forms.EmailField(required=True,widget=forms.TextInput(attrs={'class': 'form-control' , "placeholder": 'E-mail','id':'Email'}))
    password = forms.CharField(required=True,widget=forms.PasswordInput(attrs={'class': 'form-control' , "placeholder": '*********','id':'con-name'}))

class RegisterForm(UserCreationForm):
    email = forms.EmailField(required=True,widget=forms.TextInput(attrs={'class': 'form-control' , "placeholder": 'E-mail','id':'Email'}))
    password1 = forms.CharField(required=True,widget=forms.PasswordInput(attrs={'class': 'form-control' , "placeholder": '*********','id':'con-name'}))
    password2 = forms.CharField(required=True,widget=forms.PasswordInput(attrs={'class': 'form-control' , "placeholder": '*********','id':'con-name'}))

class CommentForm(forms.Form):
    commentMessage = forms.CharField(required=True,widget=forms.Textarea(attrs={'class': 'form-control',"rows":3,}))
