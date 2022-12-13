from django import forms

class LoginForm(forms.Form):
    username = forms.CharField(label='Username', max_length=25)
    password = forms.CharField(label='Password', max_length=25, widget=forms.PasswordInput())