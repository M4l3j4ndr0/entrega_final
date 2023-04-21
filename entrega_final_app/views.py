from django.shortcuts import render
from django.http import HttpResponse
from entrega_final_app.models import  Juegos #, Post
from entrega_final_app.forms import   JuegosForm , BuscarJuegosForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm #, UserChangeForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.models import User

def index(request):
    return render(request, "entrega_final_app/index.html")

def mostrar_juegos(request):
    
    juegos = Juegos.objects.all()
    total_juegos = len(juegos)
    context = {
        "juegos": juegos, 
        "total_juegos":total_juegos,
        "form": JuegosForm(),
    }
    return render(request, "entrega_final_app/juegos.html", context)

'''def alta_juegos(request):
    f = JuegosForm(request.POST)
    context = {
        "form": f
    }
    if f.is_valid():
        Juegos(nombre = f.data["nombre"], tipo = f.data["tipo"], categoria = f.data["categoria"], rating = f.data["rating"], opinion = f.data["opinion"]).save()
        context["form"] = JuegosForm()

    context["juegos"] = Juegos.objects.all()
    context["total_juegos"] = len(Juegos.objects.all())

    return render(request, "entrega_final_app/juegos_create.html", context)'''

class BuscarJuegos(ListView):
    model = Juegos
    context_object_name = "juegos"

    def get_queryset(self):
        f = BuscarJuegosForm(self.request.GET)
        if f.is_valid():
            return Juegos.objects.filter(categoria__icontains = f.data["criterio_categoria"]).all()
        return Juegos.objects.none()

class JuegosList (ListView):
    model = Juegos
    # trabaja con esto el detail ListView → Juegos.objects.all()

class JuegosDetail (DetailView):
    model = Juegos
    # trabaja con esto el detail view → Juegos.objects.get(id=pk)

class JuegosCreate(LoginRequiredMixin, CreateView):
    model = Juegos
    success_url = reverse_lazy("juegos")
    fields = '__all__' #que campos voy a utilizar para crear

'''            ['nombre',
              'tipo', 
              'rating',
              'categoria',
              'opinion',
             ] 
'''
class JuegosUpdate(LoginRequiredMixin, UpdateView):
    model = Juegos
    success_url = reverse_lazy("juegos")
    fields = ['tipo', 
              'rating',
              'categoria',
              'opinion',
              #'publisher'
             ] 
    #que campos voy a utilizar para modificar

class JuegosDelete(LoginRequiredMixin, DeleteView):
    model = Juegos
    success_url = reverse_lazy("juegos")

class SignUp(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('juegos')

class Login(LoginView):
    next_page = reverse_lazy('index')

class Logout(LogoutView):
    template_name = 'registration/logout.html'

