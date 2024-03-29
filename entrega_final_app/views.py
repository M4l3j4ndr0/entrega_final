from django.shortcuts import render
from django.http import HttpResponse
from entrega_final_app.models import  Juegos, Profile, Mensaje
from entrega_final_app.forms import   JuegosForm , BuscarJuegosForm
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from django.contrib.auth.forms import UserCreationForm 
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.auth.mixins import LoginRequiredMixin, UserPassesTestMixin

def about(request):
    return render(request, "entrega_final_app/about")

def index(request):
    context = {
        "juegos": Juegos.objects.all()
    }
    return render(request, "entrega_final_app/index.html", context)

def mostrar_juegos(request):
    
    juegos = Juegos.objects.all()
    total_juegos = len(juegos)
    context = {
        "juegos": juegos, 
        "total_juegos":total_juegos,
        "form": JuegosForm(),
    }
    return render(request, "entrega_final_app/juegos.html", context)

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

class JuegosDetail (DetailView):
    model = Juegos

class JuegosCreate(LoginRequiredMixin, CreateView):
    model = Juegos
    success_url = reverse_lazy("juegos")
    fields = ['nombre',
              'tipo', 
              'rating',
              'categoria',
              'opinion',
              'imagen'
             ] 
    def form_valid(self, form):
        form.instance.publisher = self.request.user
        return super().form_valid(form)


class JuegosUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Juegos
    success_url = reverse_lazy("juegos")
    fields = ['tipo', 
              'rating',
              'categoria',
              'opinion',
              'imagen',
              #'publisher'
             ] 
    
    def test_func(self):
        user_id = self.request.user.id
        juego_id = self.kwargs.get('pk')
        return Juegos.objects.filter(publisher = user_id, id = juego_id).exists()
    
    def handle_no_permission(self):
        return render(self.request, 'entrega_final_app/not_found.html')

class JuegosDelete(LoginRequiredMixin, UserPassesTestMixin,DeleteView):
    model = Juegos
    success_url = reverse_lazy("juegos")

    def test_func(self):
        user_id = self.request.user.id
        juego_id = self.kwargs.get('pk')
        return Juegos.objects.filter(publisher = user_id, id = juego_id).exists()

    def handle_no_permission(self):
        return render(self.request, 'entrega_final_app/not_found.html')

class SignUp(CreateView):
    form_class = UserCreationForm
    template_name = 'registration/signup.html'
    success_url = reverse_lazy('juegos')

class Login(LoginView):
    next_page = reverse_lazy('index')

class Logout(LogoutView):
    template_name = 'registration/logout.html'

class ProfileCreate(LoginRequiredMixin, CreateView):
    model = Profile
    success_url = reverse_lazy("juegos")
    fields = ['correo', 
              'imagen',
             ] 

    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class ProfileUpdate(LoginRequiredMixin, UserPassesTestMixin, UpdateView):
    model = Profile
    success_url = reverse_lazy("juegos")
    fields = ['correo', 
              'imagen',
             ] 
      
    def test_func(self):
         return Profile.objects.filter(user=self.request.user).exists()
    
    def form_valid(self, form):
        form.instance.user = self.request.user
        return super().form_valid(form)

class MensajeCreate(CreateView):
    model = Mensaje
    success_url = reverse_lazy("juegos")
    fields = '__all__'

class MensajeList(LoginRequiredMixin,ListView):
    model = Mensaje
    context_object_name = "mensajes"

    def get_queryset(self):
        return Mensaje.objects.filter(destinatario = self.request.user.id).all()
    
class MensajeDelete(LoginRequiredMixin, UserPassesTestMixin, DeleteView):
    model = Mensaje
    success_url = reverse_lazy("mensaje-list")

    def test_func(self):
        user_id = self.request.user.id
        mensaje_id = self.kwargs.get('pk')
        return Mensaje.objects.filter(destinatario = user_id).exists()
