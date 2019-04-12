from django.contrib import admin
from . models import *
# Register your models here.


class Events_modelAdmin(admin.ModelAdmin):
    list_display = ['date', 'title']

admin.site.register(Events_model, Events_modelAdmin)


class News_modelAdmin(admin.ModelAdmin):
    list_display = ['date','title']

admin.site.register(News_model, News_modelAdmin)




class faculty_modelAdmin(admin.ModelAdmin):
    list_display = ['name','phonenumber']

admin.site.register(faculty_model, faculty_modelAdmin)
