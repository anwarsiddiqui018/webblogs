from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import *

admin.site.register(Book)
admin.site.register(Comment)
admin.site.register(Category)