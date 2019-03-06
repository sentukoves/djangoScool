from django import forms

class UseForm(forms.Form):
    name = forms.CharField(label='Имя', help_text='Веедите свое имя', required=False)
    text = forms.CharField(label="Фамилия",required=False)
    rr = forms.EmailField(label="Email",required=False)
    bb = forms.FilePathField(label="Дата" , path="C:\Intel\Logs")




