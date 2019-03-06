from django import forms


class UseForm(forms.Form):
    Login = forms.CharField(max_length=16, label="Логин")
    Password = forms.CharField(max_length=16)
