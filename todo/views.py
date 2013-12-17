#-*- coding: utf-8 -*-
from django.shortcuts import render
from todo.forms import *
from todo.models import Todo
from django.shortcuts import redirect
from django.core.mail import send_mail
from djangiji.settings import MAIL_FROM
from django.contrib import messages
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth import *
from django.core.urlresolvers import reverse
from django.contrib.auth.decorators import login_required
from django.views.generic import ListView

from django.views.decorators.cache import cache_page

# @login_required
# def home(request):
#     page_title="Home"
#     todos=Todo.objects.filter(todo_author_id=request.user.id).order_by('todo_ttl')
#
#     # t=Todo.objects.get(id=7) # to generate a form directly from a model
#     # todo=TodoAddForm2(instance=t)
#     return render(request,'todo/home.html',locals())



# VUES GENERIQUES #
class ListTodos(ListView): #vue générique qui remplace "home"
    model = Todo
    context_object_name = "todos"
    template_name = "todo/home.html"

    def get_queryset(self):
        return Todo.objects.filter(user_id=self.request.user.id).order_by('todo_ttl')

    def get_context_data(self, **kwargs):
       # Nous récupérons le contexte depuis la super-classe
        context = super(ListTodos, self).get_context_data(**kwargs)
        context['page_title'] = "Home"
        return context


@login_required
def add(request):
    page_title="Add"
    hours=[i+1 for i in range(-1,24)]
    minutes=[i+1 for i in range(-1,59)]

    if request.method=="POST":
        form=TodoAddForm(request.POST)
        if form.is_valid():
            todo=Todo(
                todo_name=form.cleaned_data['todo_name'],
                todo_text=form.cleaned_data['todo_text'],
                todo_ttl=form.cleaned_data['todo_date']+" "+request.POST.get('todo_hour')+":"+request.POST.get('todo_min')+':00',
                todo_status=0,
                user_id=request.user.id
            )

            todo.save()
            messages.add_message(request, messages.SUCCESS, u'Tâche ajoutée',extra_tags="alert alert-info")
            return redirect('todo.views.add')

    else:
        form=TodoAddForm()

    return render(request,'todo/add.html',locals())

@login_required
def contact(request):
    page_title="Contact"

    if request.method=="POST":
        contact_form = ContactForm(request.POST)

        if contact_form.is_valid():
            subject="[ONLINE.NET]Message du formulaire de contact"
            msg_text="Message provenant de: "+contact_form.cleaned_data['msg_from']+"\n\n"+contact_form.cleaned_data['msg_text']
            send_mail(subject, msg_text, MAIL_FROM,['fxechappe@gmail.com'], fail_silently=False)
            messages.add_message(request, messages.SUCCESS, u'Message envoyé :-)',extra_tags="alert alert-info")
            return redirect('todo.views.contact')

    else:
        contact_form = ContactForm()

    return render(request,'todo/contact.html',locals())

@login_required
def remove(request,todo_id):
    try:
        todo=Todo.objects.get(id=todo_id)
        todo.delete()
        messages.add_message(request, messages.SUCCESS, u'Tâche supprimée',extra_tags="alert alert-info")
    except ObjectDoesNotExist:
        messages.add_message(request, messages.ERROR, u'Cette tâche n\'existe pas',extra_tags="alert alert-danger")
    return redirect('home')

@login_required
def toggle(request,todo_id):
    try:
        todo=Todo.objects.get(id=todo_id)
        if todo.todo_status == 1:
            todo.todo_status=0
        else:
            todo.todo_status=1
        todo.save()
        messages.add_message(request, messages.SUCCESS, u'Tâche modifiée!',extra_tags="alert alert-info")
    except ObjectDoesNotExist:
        messages.add_message(request, messages.ERROR, u'Cette tâche n\'existe pas',extra_tags="alert alert-danger")
    return redirect('home')

@login_required
def save(request,todo_id):
    if request.method=="POST":
        form=TodoEditForm(request.POST)
        if form.is_valid():
            try:
                todo=Todo.objects.get(id=todo_id)
                todo.todo_name=form.cleaned_data['todo_name']
                todo.todo_text=form.cleaned_data['todo_text']
                todo.save()
                messages.add_message(request, messages.SUCCESS, u'Tâche modifiée!',extra_tags="alert alert-info")
            except ObjectDoesNotExist:
                messages.add_message(request, messages.ERROR, u'Cette tâche n\'existe pas',extra_tags="alert alert-danger")
    return redirect('home')

def cnx(request):
    page_title="Login"
    if request.method=="POST":
        form=ConnexionForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password"]
            user = authenticate(username=username, password=password)
            if user:
                login(request, user)
                messages.add_message(request, messages.SUCCESS, u'Welcome home {} !'.format(username.capitalize()),extra_tags="alert alert-info text-center")
                return redirect('home')
            else:
                messages.add_message(request, messages.ERROR, u'Wrong login and/or password',extra_tags="alert alert-danger")

    else:
        form=ConnexionForm()
    return render(request, 'todo/login.html',locals())

def cnx_out(request):
    logout(request)
    return redirect(reverse(cnx))


