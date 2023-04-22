from django.db import models
from django.contrib.auth.models import User

class Juegos(models.Model):
    nombre = models.CharField(max_length=50)
    tipo = models.CharField(max_length=50)
    rating = models.CharField(max_length=2)
    categoria = models.CharField(max_length=50)
    opinion = models.TextField(max_length=500)
    publisher = models.ForeignKey(to = User, on_delete=models.CASCADE, related_name="publisher")
    imagen = models.ImageField(upload_to="posts", null=True, blank=True)
    creado_el = models.DateField(auto_now_add= True)

    def __str__(self):
        return f"id : {self.id} -- nombre: {self.nombre} -- tipo: {self.tipo} -- rating: {self.rating} / 10 -- categoria: {self.categoria} -- opinion: {self.opinion} -- creado_el: {self.creado_el}"

class Profile(models.Model):
    user = models.OneToOneField(to=User, on_delete=models.CASCADE, related_name="profile")
    correo = models.CharField(max_length=100)
    imagen = models.ImageField(upload_to="profile", null=True, blank=True)

class Mensaje(models.Model):
    mensaje = models.TextField(max_length=1000)
    email = models.EmailField(max_length=50)
    destinatario = models.ForeignKey(to=User, on_delete=models.CASCADE, related_name="destinatario")