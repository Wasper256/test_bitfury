from django.contrib import admin

from .models import Factory, FactoryOwners

admin.site.register(Factory)
admin.site.register(FactoryOwners)
