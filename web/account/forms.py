from django import forms
from django.forms import PasswordInput


class loginForm(forms.Form):
    username = forms.CharField(
        label='Username',
        required=True,
        widget=forms.TextInput())

    password = forms.CharField(
        label='Password',
        required=True,
        widget=PasswordInput())


class registerForm(forms.Form):
    
    email = forms.CharField(
        label='Email',
        required=True,
        widget=forms.TextInput()
    )

    username = forms.CharField(
        label='Username',
        required=True,
        widget=forms.TextInput())

    password = forms.CharField(
        label='Password',
        required=True,
        widget=PasswordInput()
    )

    confirm_password = forms.CharField(
        label='Confirm Password',
        required=True,
        widget=PasswordInput())
