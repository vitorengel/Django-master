from django import forms

class CarForm(forms.Form):
    model = forms.CharField(max_length=200)