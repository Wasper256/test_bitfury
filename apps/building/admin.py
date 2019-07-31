from django.contrib import admin
from .models import Building, BuildingOwners


class BuildingAdmin(admin.ModelAdmin):
    pass


class BuildingOwnersAdmin(admin.ModelAdmin):
    pass


admin.site.register(Building, BuildingAdmin)
admin.site.register(BuildingOwners, BuildingOwnersAdmin)
