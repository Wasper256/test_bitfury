
from rest_framework.exceptions import ValidationError
from django.db.models import Sum


def share_custom_validator(self, attrs, Model):
    qs = Model.objects.filter(
        object=self.initial_data.get('object')).exclude(
        shareholder=self.initial_data.get(
            'shareholder')).aggregate(Sum('share'))
    if not qs['share__sum']:
        qs['share__sum'] = 0
    if attrs + qs['share__sum'] > 1:
        raise ValidationError("Error! Total share can't be more than 100%")


def calculate_relative_share(object_id, Model):
    shares = Model.objects.filter(object=object_id).values_list(
        'share', flat=True)
    share = (1 - sum([x for x in shares if x]))/len([x for x in shares if x is None])
    return share


def custom_retrieve(kwargs, request, response):
    """
    Custom retrieve serializer.
    Checks is_owner and calculate relative share if there are users without
    exact share.
    """
    shareholders_data = response.data['shareholders']
    if request.user.id:
        shareholders_list = [i['shareholder'] for i in shareholders_data]
        if request.user.id in shareholders_list:
            is_owner = True
        else:
            is_owner = False
        response.data['is_owner'] = is_owner
    shareholders_with_relative_share_exists = [
        i['share'] for i in shareholders_data if i['share'] is None]
    if shareholders_with_relative_share_exists:
        shareholders_with_relative_share = [
            i['shareholder'] for i in shareholders_data
            if i['share'] is None]
        share = calculate_relative_share(
            kwargs['pk'],
            response.data.serializer.Meta.model.owners.field.model)
        for i in response.data['shareholders']:
            if i['shareholder'] in shareholders_with_relative_share:
                i['share'] = share