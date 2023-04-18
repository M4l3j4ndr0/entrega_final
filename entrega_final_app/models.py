from django.db import models

class Notas(models.Model):
    alumno = models.TextField(max_length=100)
    materia = models.TextField(max_length=100)
    fecha_parcial = models.DateTimeField(auto_now_add=True)
    nota_parcial = models.TextField(max_length=2)

    def __str__(self):
        return f"id de registro: {self.id} -- Materia: {self.materia}   --   Alumno: {self.alumno}   --   fecha de parcial: {self.fecha_parcial}  --   nota de parcial: {self.nota_parcial}"


class Usuario(models.Model):
    usuario = models.TextField(max_length=100)
    nombre = models.TextField(max_length=100)
    apellido = models.TextField(max_length=100)
    fecha_nacimiento = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"id usuario: {self.id} -- username: {self.usuario} -- nombre usuario: {self.nombre} -- apellido usuario: {self.apellido} -- fecha nacimiento: {self.fecha_nacimiento}"
    
class Elementos(models.Model):
    elemento = models.TextField(max_length=50)
    tipo = models.TextField(max_length=50)
    categoria = models.TextField(max_length=50)

    def __str__(self):
        return f"id registro: {self.id} -- elemento: {self.elemento} -- tipo: {self.tipo} -- categoria: {self.categoria}"
