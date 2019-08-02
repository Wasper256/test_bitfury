from django.contrib import admin

from .models import Building, BuildingOwners


admin.site.register(Building)
admin.site.register(BuildingOwners)
