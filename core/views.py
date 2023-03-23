from django.utils.timezone import now
from rest_framework.authtoken.models import Token
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework.viewsets import ReadOnlyModelViewSet, ModelViewSet
from rest_framework.authentication import SessionAuthentication, TokenAuthentication
from rest_framework.permissions import IsAuthenticated, DjangoModelPermissions
from rest_framework.generics import GenericAPIView
from core import models
from core import filters
from core import serializers


class RegisterUser(GenericAPIView):
    queryset = models.User
    serializer_class = serializers.RegisteUser

    def __pos__(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = models.User.objects.create_user(
            username=serializer.validated_data['username'],
            password=serializer.validated_data['password']
        )
        token = Token.objects.create(user=user)
        return Response



class LoginUser(GenericAPIView):
    queryset = models.User
    serializer_class = serializers.LoginUser

    def __pos__(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        token = Token.objects.get(user_username=serializer.validated_data['username'])
        return Response({'token': token.key})


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


    def perform_create(self, serializer):
        serializer.validated_data['user'] = self.request.user
        serializer.save()


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


