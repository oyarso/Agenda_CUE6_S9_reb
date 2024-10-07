from django.db import models 
from django.conf import settings 
# class BoardsModel2(models.Model): 
#     titulo = models.CharField(max_length = 150) 
#     autor = models.CharField(max_length = 150) 
#     valoracion = models.IntegerField(range(0,10000)) 
# def __str__(self): 
#     return self.titulo


class BoardsModel(models.Model):
    # Campos del modelo 
    titulo = models.CharField(max_length = 200)
    descripcion = models.TextField()
    modificado = models.DateTimeField(auto_now_add = True)
    
    class Meta:
        permissions = (
            ("es_miembro_1", "Es miembro con prioridad 1"),
        )

    def __str__(self):
        return self.titulo