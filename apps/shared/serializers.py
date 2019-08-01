from rest_framework import serializers
from .models import OwnershipAbstract
from apps.building.models import BuildingOwners


# class BaseShareholdersRetrieveSerializer(serializers.Serializer):
#     username = serializers.CharField(read_only=True,
#                                      source="shareholder.username")
#     first_name = serializers.CharField(read_only=True,
#                                        source="shareholder.first_name")
#
#     class Meta:
#         model = OwnershipAbstract
#         fields = ('shareholder', 'username', 'first_name', 'share')
#         abstract = True


class DeleteShareSerializer(serializers.Serializer):
    shareholder = serializers.IntegerField(allow_null=False)
    object = serializers.IntegerField(allow_null=False)