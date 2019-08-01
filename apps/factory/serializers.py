from rest_framework import serializers

from apps.shared.utils import share_custom_validator
from .models import Factory, FactoryOwners


class FactoryShareholdersRetrieveSerializer(serializers.ModelSerializer):
    username = serializers.CharField(read_only=True,
                                     source="shareholder.username")
    first_name = serializers.CharField(read_only=True,
                                       source="shareholder.first_name")

    class Meta:
        model = FactoryOwners
        fields = ('shareholder', 'username', 'first_name', 'share')


class FactoryBaseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Factory
        fields = ('id', 'name', 'location')


class FactoryRetrieveSerializer(serializers.ModelSerializer):
    shareholders = serializers.SerializerMethodField()

    class Meta:
        model = Factory
        fields = ('id', 'name', 'location', 'shareholders',)
        read_only_fields = ('shareholders', )

    def get_shareholders(self, obj):
        return FactoryShareholdersRetrieveSerializer(
            obj.owners.model.objects.filter(
                object=self.instance).select_related('shareholder'),
            many=True, context=self.context).data


class CreateUpdateShareSerializer(serializers.ModelSerializer):
    class Meta:
        model = FactoryOwners
        fields = ('shareholder', 'share', 'object')

    def validate_share(self, attrs):
        attrs = super().validate(attrs)
        share_custom_validator(self, attrs, FactoryOwners)
        return attrs
