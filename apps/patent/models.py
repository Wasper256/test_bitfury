from django.db import models

from apps.shared.models import OwnershipAbstract


class Patent(models.Model):
    name = models.CharField(max_length=100)
    tech_description = models.TextField(null=True, blank=True)


class PatentOwners(OwnershipAbstract):
    object = models.ForeignKey(Patent, on_delete=models.CASCADE,
                               related_name='owners')