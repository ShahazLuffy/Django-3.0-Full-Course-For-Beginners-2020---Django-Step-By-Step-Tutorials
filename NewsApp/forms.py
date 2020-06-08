from django import forms

class RegistrationForm(forms.Form):
    username = forms.CharField(max_length=40)
    password = forms.CharField(max_length=100)
    email = forms.CharField(max_length=44)
    phone = forms.CharField(max_length=44)