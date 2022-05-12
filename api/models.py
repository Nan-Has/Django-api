from django.db import models

Choix_Abonnement = (
    ('Access', 'Access'),
    ('Evasion', 'Evasion'),
    ('Essentiel+', 'Essentiel+'),
    ('Access+', 'Access+'),
    ('Evasion+', 'Evasion+'),
    ('Tout Canal', 'Tout canal')
)

class client(models.Model):
    Nom = models.CharField(max_length=100)
    Option_Abonnement = models.CharField(max_length=50, choices=Choix_Abonnement, default='Access')
    Date_Abonnement = models.DateField(default='2022-01-01')
    Numero_Abonnement = models.CharField(max_length=100)

    def __str__(self):
        return self.Nom