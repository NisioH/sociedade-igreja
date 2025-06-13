from django.db import models
from django.contrib.auth.models import User

class Sociedade(models.Model):
    nome = models.CharField(max_length=100)

class Membro(models.Model):
    usuario = models.OneToOneField(User, on_delete=models.CASCADE)
    sociedade = models.ForeignKey(Sociedade, on_delete=models.CASCADE)
    cargo = models.CharField(
        max_length=50,
        choices=[
            ('Presisdente', 'Presidente'),
            ('Vice-Presidente', 'Vice-Presidente'),
            ('1º Secretário', '1ºSecretário'),
            ('2º Secretário', '2º Secretário'),
            ('Membro', 'Membro'),
        ]
    )
