from django.db import models

''' #ver si se puede adaptar
class Post(models.Model):
    carousel_caption_title = models.CharField(max_length=30)
    carousel_caption_description = models.CharField(max_length=80)
    heading  = models.CharField(max_length=15)
    description = models.CharField(max_length=120)

    def __str__(self):
        return f"{self.id} -- {self.carousel_caption_title} -- {self.carousel_caption_description}"
   '''
class Juegos(models.Model):
    nombre = models.TextField(max_length=50)
    tipo = models.TextField(max_length=50)
    rating = models.TextField(max_length=2)
    categoria = models.TextField(max_length=50)
    opinion = models.TextField(max_length=500)

    def __str__(self):
        return f"id : {self.id} -- nombre: {self.nombre} -- tipo: {self.tipo} -- rating: {self.rating} / 10 -- categoria: {self.categoria} -- opinion: {self.opinion}"
