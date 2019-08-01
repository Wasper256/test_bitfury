from django.db import models

from apps.shared.models import OwnershipAbstract


class Building(models.Model):
    name = models.CharField(max_length=100)
    address = models.CharField(max_length=255)
    area = models.DecimalField(max_digits=10, decimal_places=2)


class BuildingOwners(OwnershipAbstract):
    object = models.ForeignKey(Building, on_delete=models.CASCADE,
                               related_name='owners')
