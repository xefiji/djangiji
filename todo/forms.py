#-*- coding: utf-8 -*-
from django import forms
from models import Todo

# class TodoAddForm2(forms.ModelForm): # to generate a form directly from a model
#     class Meta:
#         model=Todo
#         exclude=("todo_author_id",)

class TodoAddForm(forms.Form):
    todo_name=forms.CharField(max_length=255,
                              widget=forms.TextInput(
                                  attrs={
                                      'class':'form-control input-lg'
                                  }
                              )
    )
    todo_text=forms.CharField(required=False,widget=forms.Textarea(
        attrs={
            'class':'form-control'
        }
    )
    )
    todo_date=forms.CharField(widget=forms.TextInput(
        attrs={
            'class':'form-control datepicker'
        }
    )
    )

    # todo_status=forms.CharField(widget=forms.HiddenInput, initial=0)
    # todo_author_id=forms.CharField(widget=forms.HiddenInput(
    #     attrs={
    #         'value':request.user.id
    #     }
    # ))

class TodoEditForm(forms.Form):
    todo_name=forms.CharField(max_length=255)
    todo_text=forms.CharField(required=False,max_length=255)



class ContactForm(forms.Form):
    msg_from=forms.EmailField(max_length=255,
                              widget=forms.EmailInput(
                                  attrs={
                                      'class':'form-control input-lg',
                                      'placeholder':'votre adresse mail',
                                  }
                              )
    )
    msg_text=forms.CharField(widget=forms.Textarea(
        attrs={
            'class':'form-control',
            'placeholder':'votre message'
        }
    )
    )

class ConnexionForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(
        attrs={
            'class':'form-control',
            # 'placeholder':'login'
        }))
    password=forms.CharField(widget=forms.PasswordInput(
        attrs={
            'class':'form-control',
            # 'placeholder':'password'
        }))