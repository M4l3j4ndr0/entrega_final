from django.db import models
   
class Juegos(models.Model):
    nombre = models.TextField(max_length=50)
    tipo = models.TextField(max_length=50)
    rating = models.TextField(max_length=2)
    categoria = models.TextField(max_length=50)
    opinion = models.TextField(max_length=100)

    def __str__(self):
        return f"id registro: {self.id} -- nombre: {self.nombre} -- tipo: {self.tipo} -- tipo: {self.rating} -- categoria: {self.categoria} -- categoria: {self.opinion}"
