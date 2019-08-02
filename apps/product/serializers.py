from rest_framework import serializers

from apps.shared.serializers import BaseShareholdersRetrieveSerializer
from apps.shared.utils import share_custom_validator
from .models import Product, ProductOwners


class ProductShareholdersRetrieveSerializer(
        BaseShareholdersRetrieveSerializer):
    class Meta:
        model = ProductOwners
        fields = ('shareholder', 'username', 'first_name', 'share')


class ProductBaseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'factory', 'patent')


class ProductRetrieveSerializer(serializers.ModelSerializer):
    shareholders = serializers.SerializerMethodField()

    class Meta:
        model = Product
        fields = ('id', 'name', 'description', 'factory', 'patent',
                  'shareholders')
        read_only_fields = ('shareholders', )

    def get_shareholders(self, obj):
        return ProductShareholdersRetrieveSerializer(
            obj.owners.model.objects.filter(
                shared_object=self.instance).select_related('shareholder'),
            many=True, context=self.context).data


class CreateUpdateShareSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductOwners
        fields = ('shareholder', 'share', 'shared_object')

    def validate_share(self, attrs):
        attrs = super().validate(attrs)
        share_custom_validator(self, attrs, ProductOwners)
        return attrs
