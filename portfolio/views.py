#-*- coding: utf-8 -*-
from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
from portfolio.models import User
from portfolio.forms import ContactForm
from django.core.mail import send_mail


def tpl(request):
    return render(request, 'blog/tpl.html', {'current_date': datetime.now()})

def contact(request):
    if request.method=="POST":
        contact_form=ContactForm(request.POST)
        if contact_form.is_valid():
            sujet = contact_form.cleaned_data['sujet']
            message = contact_form.cleaned_data['message']
            email = contact_form.cleaned_data['email']
            renvoi = contact_form.cleaned_data['renvoi']

    else:
        contact_form=ContactForm()

    return render(request,'portfolio/contact.html',locals())


def home(request):
    text = "<h2>HELLOOO</h2> <h1>WOOOORLD</h1>"
    return HttpResponse(text)

def view_user(request,user_id):
    current_date=datetime.now()
    users=User.objects.filter(id=user_id)
    text = "Détails pour l'user {}".format(user_id)
    return render(request,'portfolio/tpl.html',locals())

def view_all(request):
    user=User(nom="Chaaap",prenom="Fiiiix",email="xefihotmail.fr",password="dqes",dob="1980-07-01")
    user.save()
    current_date=datetime.now()
    users=User.objects.all()
    return render(request,'portfolio/tpl.html',locals())

def tpl(request):
    current_date=datetime.now()
    user_id=23
    return render(request,'portfolio/tpl.html',locals())