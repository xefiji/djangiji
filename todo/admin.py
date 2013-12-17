# -*- coding: utf-8 -*-
from django.contrib import admin
from todo.models import Todo

class TodoAdmin(admin.ModelAdmin):
   list_display   = ('id', 'todo_name', 'todo_text','user','todo_status', 'todo_ttl','todo_tstp_created','todo_tstp_updated')
   # list_filter    = ('id','nom',)
   # date_hierarchy = 'id'
   ordering       = ('id',)
   search_fields  = ('todo_name', 'todo_text')

admin.site.register(Todo,TodoAdmin)