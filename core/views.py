from django.utils.timezone import now
from rest_framework.decorators import action
from rest_framework.response import Response
from  rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from  rest_framework.permissions import IsAuthenticated, DjangoModelPermissions
from rest_framework.generics import GenericAPIView
from core import models
from core import filters
from core import serializers


class RegisterUser(GenericAPIView):
    queryset = models.User

    def __pos__(self):
        #TODO
        pass


class TagViewSet(ReadOnlyModelViewSet):
    authentication_classes = (SessionAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated, DjangoModelPermissions)
    queryset = models.Tag.objects.all()
    serializer_class = serializers.Tag
    filterset_class = filters.Tag

class ItemViewSet(ModelViewSet):
    authentication_classes = (SessionAuthentication, TokenAuthentication)
    permission_classes = (IsAuthenticated, DjangoModelPermissions)
    serializer_class = serializers.Item
    filterset_class = filters.Item

    def get_queryset(self):
        return models.Item.objects.filter(user=self.request.user)


    @action(detail=True, methods=['post', 'put', 'patch'])
    def set_done(self, reuest, pk=None):
        models.Item.objects.filter(pk=pk, done__isnull=True).update(done=now())
        return Response({'message': 'ok'})

    @action(detail=True, methods=['post', 'put', 'patch'])
    def unset_done(self, reuest, pk=None):
        item: models.Item = self.get_object()
        if item.done:
            item.done = None
            item.save(update_fields=['done'])
        serializer = serializers.Item(instance=item)
        return Response(serializer.data)


