from django.db import models

class Autor(models.Model):
    nombre=models.CharField(max_length=100)
    pais=models.CharField(max_length=100)

    def __str__(self):
        return f"Autor: {self.nombre}"

class Libro(models.Model):
    titulo = models.CharField(max_length=100)
    fk_autor = models.ForeignKey(Autor,on_delete=models.CASCADE)
    year = models.IntegerField()
    editorial = models.CharField(max_length=100)

    def __str__(self):
        return f"Libro: {self.titulo}"


