from django.db import models

from apps.building.models import Building
from apps.shared.models import OwnershipAbstract


class Factory(models.Model):
    name = models.CharField(max_length=100)
    location = models.ForeignKey(Building, on_delete=models.CASCADE)


class FactoryOwners(OwnershipAbstract):
    object = models.ForeignKey(Factory, on_delete=models.CASCADE,
                               related_name='owners')
