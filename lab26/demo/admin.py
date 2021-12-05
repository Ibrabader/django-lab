from django.contrib import admin
from .models import demo
# Register your models here.

@admin.register(demo)
class AdminThing(admin.ModelAdmin):
    list_display = ['title']