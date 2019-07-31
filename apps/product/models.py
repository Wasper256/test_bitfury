from django.db import models

from apps.factory.models import Factory
from apps.patent.models import Patent
from apps.shared.models import OwnershipAbstract


class Product(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    factory = models.ForeignKey(Factory, on_delete=models.CASCADE)
    patent = models.ManyToManyField(Patent)


class ProductOwners(OwnershipAbstract):
    object = models.ForeignKey(Product, on_delete=models.CASCADE)
