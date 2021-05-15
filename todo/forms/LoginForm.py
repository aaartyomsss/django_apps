from django import forms

class LoginForm(forms.Form):
    attrs = {
        'type': 'password'
    }
    username = forms.CharField(label='Username',)
    password = forms.CharField(widget=forms.TextInput(attrs=attrs))
