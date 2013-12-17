from django.contrib import admin
from portfolio.models import User
# Register your models here.

class UserAdmin(admin.ModelAdmin):
   list_display   = ('id', 'nom', 'prenom', 'email', 'dob')
   # list_filter    = ('id','nom',)
   # date_hierarchy = 'id'
   ordering       = ('id', )
   search_fields  = ('email', 'nom'), 'prenom'

admin.site.register(User,UserAdmin)