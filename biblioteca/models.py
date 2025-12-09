from django.db import models

class Category(models.Model):
    nombre = models.CharField(max_length=50)

    def __str__(self):
        return self.nombre


class Model3D(models.Model):
    nombre = models.CharField(max_length=100)
    descripcion = models.TextField()
    url_archivo = models.URLField(help_text="Link a Thingiverse, Cults o Google Drive")
    categoria = models.ForeignKey(Category, on_delete=models.CASCADE)
    nivel = models.CharField(max_length=20, choices=[
        ('Básico', 'Básico'),
        ('Intermedio', 'Intermedio'),
        ('Avanzado', 'Avanzado'),
    ])

    def __str__(self):
        return self.nombre
