#-*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User

class Todo(models.Model):
    todo_name=models.CharField(max_length=255)
    todo_text=models.TextField()
    todo_status=models.IntegerField()
    user=models.ForeignKey(User)
    todo_ttl=models.DateTimeField()
    todo_tstp_created=models.DateTimeField(auto_now_add=True)
    todo_tstp_updated=models.DateTimeField(auto_now=True)
    def __unicode__(self):
        return u'Todo %d : %s' % (self.id, self.todo_name)
