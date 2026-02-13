from django.db import models

# Create your models here.
class Catalogo(models.Model):
    nome = models.CharField(max_length=100)
    preco =  models.DecimalField(max_digits=8, decimal_places=2)
    criado_em = models.DateField(auto_now_add=True)

    def __str__(self):
     return self.nome

