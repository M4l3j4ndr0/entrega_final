from django.shortcuts import render
from django.http import HttpResponse
from entrega_final_app.models import Notas, Usuario, Elementos
from entrega_final_app.forms import NotasForm, BuscarNotasForm, UsuariosForm,BuscarUsuariosForm, ElementosForm, BuscarElementosForm
from django.views.generic import ListView

def mostrar_notas(request):
    
    notas = Notas.objects.all()
    total_notas = len(notas)
    context = {
        "notas": notas, 
        "total_notas":total_notas,
        "form": NotasForm(),
    }
    return render(request, "entrega_final_app/notas.html", context)


def alta_notas(request):
    f = NotasForm(request.POST)
    context = {
        "form": f
    }
    if f.is_valid():
        Notas(alumno = f.data["alumno"], materia = f.data["materia"], fecha_parcial = f.data["fecha_parcial"], nota_parcial = f.data["nota_parcial"]).save()
        context["form"] = NotasForm()

    context["notas"] = Notas.objects.all()
    context["total_notas"] = len(Notas.objects.all())

    return render(request, "entrega_final_app/notas_create.html", context)


class BuscarNotas(ListView):
    model = Notas
    context_object_name = "notas"

    def get_queryset(self):
        f = BuscarNotasForm(self.request.GET)
        if f.is_valid():
            return Notas.objects.filter(materia__icontains = f.data["criterio_materia"]).all()
        return Notas.objects.none()
    


def mostrar_usuarios(request):
    
    usuarios = Usuario.objects.all()
    total_usuarios = len(usuarios)
    context = {
        "usuarios": usuarios, 
        "total_usuarios":total_usuarios,
        "form": UsuariosForm(),
    }
    return render(request, "entrega_final_app/usuarios.html", context)

def alta_usuarios(request):
    f = UsuariosForm(request.POST)
    context = {
        "form": f
    }
    if f.is_valid():
        Usuario(usuario = f.data["usuario"], nombre = f.data["nombre"], apellido = f.data["apellido"], fecha_nacimiento = f.data["fecha_nacimiento"]).save()
        context["form"] = NotasForm()

    context["usuarios"] = Usuario.objects.all()
    context["total_usuarios"] = len(Usuario.objects.all())

    return render(request, "entrega_final_app/usuario_create.html", context)

class BuscarUsuarios(ListView):
    model = Usuario
    context_object_name = "usuarios"

    def get_queryset(self):
        f = BuscarUsuariosForm(self.request.GET)
        if f.is_valid():
            return Usuario.objects.filter(usuario__icontains = f.data["criterio_usuario"]).all()
        return Usuario.objects.none()
    
def mostrar_elementos(request):
    
    elementos = Elementos.objects.all()
    total_elementos = len(elementos)
    context = {
        "elementos": elementos, 
        "total_elementos":total_elementos,
        "form": ElementosForm(),
    }
    return render(request, "entrega_final_app/elementos.html", context)

def alta_elementos(request):
    f = ElementosForm(request.POST)
    context = {
        "form": f
    }
    if f.is_valid():
        Elementos(elemento = f.data["elemento"], tipo = f.data["tipo"], categoria = f.data["categoria"]).save()
        context["form"] = ElementosForm()

    context["elementos"] = Elementos.objects.all()
    context["total_elementos"] = len(Elementos.objects.all())

    return render(request, "entrega_final_app/elementos_create.html", context)

class BuscarElementos(ListView):
    model = Elementos
    context_object_name = "elementos"

    def get_queryset(self):
        f = BuscarElementosForm(self.request.GET)
        if f.is_valid():
            return Elementos.objects.filter(categoria__icontains = f.data["criterio_categoria"]).all()
        return Elementos.objects.none()