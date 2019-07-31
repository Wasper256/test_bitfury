from django.contrib import admin
from .models import Patent, PatentOwners


class PatentAdmin(admin.ModelAdmin):
    pass


class PatentOwnersAdmin(admin.ModelAdmin):
    pass


admin.site.register(Patent, PatentAdmin)
admin.site.register(PatentOwners, PatentOwnersAdmin)
