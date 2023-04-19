from django.shortcuts import render
from django.http import HttpResponse
from entrega_final_app.models import  Juegos
from entrega_final_app.forms import   JuegosForm, BuscarJuegosForm
from django.views.generic import ListView

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

def alta_juegos(request):
    f = JuegosForm(request.POST)
    context = {
        "form": f
    }
    if f.is_valid():
        Juegos(juego = f.data["juego"], tipo = f.data["tipo"], categoria = f.data["categoria"], rating = f.rating["rating"], opinion = f.opinion["opinion"] ).save()
        context["form"] = JuegosForm()

    context["juegos"] = Juegos.objects.all()
    context["total_juegos"] = len(Juegos.objects.all())

    return render(request, "entrega_final_app/juegos_create.html", context)

class BuscarJuegos(ListView):
    model = Juegos
    context_object_name = "juegos"

    def get_queryset(self):
        f = BuscarJuegosForm(self.request.GET)
        if f.is_valid():
            return Juegos.objects.filter(categoria__icontains = f.data["criterio_categoria"]).all()
        return Juegos.objects.none()