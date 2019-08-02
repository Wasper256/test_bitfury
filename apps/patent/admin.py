from django.contrib import admin

from .models import Patent, PatentOwners

admin.site.register(Patent)
admin.site.register(PatentOwners)
