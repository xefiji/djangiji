#-*- coding: utf-8 -*-
from django.db import models

class User(models.Model):
    nom = models.CharField(max_length=50)
    prenom = models.CharField(max_length=50)
    email = models.EmailField()
    password = models.CharField(max_length=255)
    dob = models.DateTimeField(auto_now_add=False, auto_now=False, verbose_name="Date de naissance")

    def __unicode__(self):
        """
        Cette méthode que nous définirons dans tous les modèles
        nous permettra de reconnaître facilement les différents objets que nous
        traiterons plus tard et dans l'administration
        """
        return u"%s" % self.nom
