from django.db import models


class Blog(models.Model):
    titulo = models.CharField(max_length= 200)
    autor = models.CharField(max_length=200)
    contenido = models.TextField()
    id = models.BigAutoField(primary_key=True)

    

    def __str__(self):
        return self.titulo
