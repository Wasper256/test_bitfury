from rest_framework import serializers

from apps.shared.serializers import BaseShareholdersRetrieveSerializer
from apps.shared.utils import share_custom_validator
from .models import Patent, PatentOwners


class PatentShareholdersRetrieveSerializer(
        BaseShareholdersRetrieveSerializer):
    class Meta:
        model = PatentOwners
        fields = ('shareholder', 'username', 'first_name', 'share')


class PatentBaseSerializer(serializers.ModelSerializer):

    class Meta:
        model = Patent
        fields = ('id', 'name', 'tech_description')


class PatentRetrieveSerializer(serializers.ModelSerializer):
    shareholders = serializers.SerializerMethodField()

    class Meta:
        model = Patent
        fields = ('id', 'name', 'tech_description', 'shareholders',)
        read_only_fields = ('shareholders', )

    def get_shareholders(self, obj):
        return PatentShareholdersRetrieveSerializer(
            obj.owners.model.objects.filter(
                object=self.instance).select_related('shareholder'),
            many=True, context=self.context).data


class CreateUpdateShareSerializer(serializers.ModelSerializer):
    class Meta:
        model = PatentOwners
        fields = ('shareholder', 'share', 'object')

    def validate_share(self, attrs):
        attrs = super().validate(attrs)
        share_custom_validator(self, attrs, PatentOwners)
        return attrs
