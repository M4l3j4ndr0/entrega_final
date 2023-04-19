from django import forms

class JuegosForm (forms.Form):
    nombre = forms.CharField(max_length=50)
    tipo = forms.CharField(max_length=50)
    rating = forms.CharField(max_length=2)
    categoria = forms.CharField(max_length=50)
    opinion = forms.CharField(max_length=100)

class BuscarJuegosForm(forms.Form):
    criterio_categoria = forms.CharField(max_length=50)