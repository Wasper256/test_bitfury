from rest_framework import serializers

from apps.shared.serializers import BaseShareholdersRetrieveSerializer
from apps.shared.utils import share_custom_validator
from .models import Building, BuildingOwners


class BuildingShareholdersRetrieveSerializer(
        BaseShareholdersRetrieveSerializer):
    class Meta:
        model = BuildingOwners
        fields = ('shareholder', 'username', 'first_name', 'share')


class BuildingBaseSerializer(serializers.ModelSerializer):
    class Meta:
        model = Building
        fields = ('id', 'name', 'address', 'area',)


class BuildingRetrieveSerializer(serializers.ModelSerializer):
    shareholders = serializers.SerializerMethodField()

    class Meta:
        model = Building
        fields = ('id', 'name', 'address', 'area', 'shareholders')
        read_only_fields = ('shareholders',)

    def get_shareholders(self, obj):
        return BuildingShareholdersRetrieveSerializer(
            obj.owners.model.objects.filter(
                object=self.instance).select_related('shareholder'),
            many=True, context=self.context).data


class CreateUpdateShareSerializer(serializers.ModelSerializer):
    class Meta:
        model = BuildingOwners
        fields = ('shareholder', 'share', 'object')

    def validate_share(self, attrs):
        attrs = super().validate(attrs)
        share_custom_validator(self, attrs, BuildingOwners)
        return attrs
