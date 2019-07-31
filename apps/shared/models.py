from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.db import models


class OwnershipAbstract(models.Model):
    shareholder = models.ForeignKey(User, on_delete=models.CASCADE)
    # if share is null, then will be equal with other owners
    # if it is single holder and empty then share == 100%
    share = models.DecimalField(blank=True, null=True, decimal_places=2,
                                max_digits=2)
    object = models.IntegerField()

    class Meta:
        abstract = True
        unique_together = ['shareholder', 'object']
