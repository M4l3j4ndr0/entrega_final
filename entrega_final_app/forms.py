from django import forms

class NotasForm (forms.Form):
    alumno = forms.CharField(max_length=100)
    materia = forms.CharField(max_length=100)
    fecha_parcial = forms.DateField()
    nota_parcial = forms.CharField(max_length=2)

class BuscarNotasForm(forms.Form):
    criterio_materia = forms.CharField(max_length=100)


class UsuariosForm(forms.Form):
    usuario = forms.CharField(max_length=100)
    nombre = forms.CharField(max_length=100)
    apellido = forms.CharField(max_length=100)
    fecha_nacimiento = forms.DateField()
    

class BuscarUsuariosForm(forms.Form):
    criterio_usuario = forms.CharField(max_length=100)

class ElementosForm (forms.Form):
    elemento = forms.CharField(max_length=50)
    tipo = forms.CharField(max_length=50)
    categoria = forms.CharField(max_length=50)

class BuscarElementosForm(forms.Form):
    criterio_categoria = forms.CharField(max_length=50)