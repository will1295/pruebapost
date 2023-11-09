from django import forms

class NameForm(forms.Form):
    nombre = forms.CharField(label="Escribe tu nombre ",max_length=100)