from rest_framework import serializers

from .models import OwnershipAbstract


class BaseShareholdersRetrieveSerializer(serializers.Serializer):
    username = serializers.CharField(read_only=True,
                                     source="shareholder.username")
    first_name = serializers.CharField(read_only=True,
                                       source="shareholder.first_name")
    shareholder = serializers.CharField(read_only=True,
                                        source="shareholder.id")
    share = serializers.DecimalField(read_only=True, max_digits=3,
                                     decimal_places=2)

    class Meta:
        model = OwnershipAbstract
        fields = ('shareholder', 'username', 'first_name', 'share')
        abstract = True


class DeleteShareSerializer(serializers.Serializer):
    shareholder = serializers.IntegerField(allow_null=False)
    shared_object = serializers.IntegerField(allow_null=False)