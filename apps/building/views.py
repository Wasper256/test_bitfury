from rest_framework import status
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from apps.shared.utils import custom_retrieve
from apps.shared.serializers import DeleteShareSerializer
from .models import Building, BuildingOwners
from .serializers import (
    BuildingRetrieveSerializer, BuildingBaseSerializer,
    CreateUpdateShareSerializer
)


class BuildingViewSet(viewsets.ModelViewSet):
    queryset = Building.objects.filter()

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return BuildingRetrieveSerializer
        return BuildingBaseSerializer

    def retrieve(self, request, *args, **kwargs):
        response = super().retrieve(request, *args, **kwargs)
        custom_retrieve(kwargs, request, response)
        return response

    @action(detail=False, name='update', methods=['post', 'put'])
    def update_share(self, request, *args, **kwargs):
        serializer = CreateUpdateShareSerializer(data=request.data)
        valid = serializer.is_valid()
        if valid:
            serializer.save()
        # solution to make update and create in single action endpoint
        elif 'non_field_errors' in serializer.errors:
            if serializer.errors.get('non_field_errors')[0] == (
                    'The fields shareholder, object must make a unique set.'):
                BuildingOwners.objects.filter(
                    object=serializer.initial_data.get('object'),
                    shareholder=serializer.initial_data.get('shareholder'))\
                    .update(share=serializer.initial_data.get('share'))
        else:
            serializer.is_valid(raise_exception=True)
        headers = self.get_success_headers(serializer.validated_data)
        return Response(serializer.data, status=status.HTTP_200_OK,
                        headers=headers)

    @action(detail=False, name='delete', methods=['delete'])
    def delete_share(self, request, *args, **kwargs):
        serializer = DeleteShareSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        deleted = BuildingOwners.objects.filter(
            object=serializer.initial_data.get('object'),
            shareholder=serializer.initial_data.get('shareholder')).delete()
        if deleted[0]:
            return Response({"success": "Successfully deleted"},
                            status=status.HTTP_204_NO_CONTENT)
        elif not deleted[0]:
            return Response({"error": "No such share found"},
                            status=status.HTTP_404_NOT_FOUND)
