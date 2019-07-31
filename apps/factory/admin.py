from django.contrib import admin
from .models import Factory, FactoryOwners


class FactoryAdmin(admin.ModelAdmin):
    pass


class FactoryOwnersAdmin(admin.ModelAdmin):
    pass


admin.site.register(Factory, FactoryAdmin)
admin.site.register(FactoryOwners, FactoryOwnersAdmin)
