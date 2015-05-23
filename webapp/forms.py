from django import forms

class RefreshButton(forms.Form):
    button = forms.CharField(label='', max_length=100)

class PickButton(forms.Form):
    pick = forms.CharField(label='', max_length=100)

class Filter(forms.Form):
    title = forms.CharField(label='Titulo', max_length=100)
    date = forms.CharField(label='Fecha', max_length=100)
    price = forms.IntegerField(label='Precio')