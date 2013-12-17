#-*- coding: utf-8 -*-
__author__ = 'fechappe'
from django import forms

class ContactForm(forms.Form):
    sujet = forms.CharField(max_length=100)
    email=forms.EmailField(label=u"Votre adresse mail")
    message=forms.CharField(widget=forms.Textarea)
    renvoi = forms.BooleanField(help_text=u"Cochez si vous souhaitez obtenir une copie du mail envoyé.", required=False)
