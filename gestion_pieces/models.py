from django.db import models

# Create your models here.
# gestion_pieces/models.py
from django.db import models

class PieceDisparue(models.Model):
    nom = models.CharField(max_length=100)
    description = models.TextField()
    date_de_declaration = models.DateField(auto_now_add=True)
    image = models.ImageField(upload_to='images/', null=True, blank=True)

    def __str__(self):
        return self.nom