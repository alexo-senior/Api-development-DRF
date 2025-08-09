from django.contrib import admin

from .models import Blog, Comment

#se registran los modelos en el admin y se realizan las migraciones correspondientes

admin.site.register(Blog)
admin.site.register(Comment)
