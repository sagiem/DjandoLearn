from django.urls import path, include
from rest_framework.routers import DefaultRouter
import core.views

app_name = 'core'

urlpatterns = [
    path('login/', core.views.LoginUser.as_view(), name='user_login'),
    path('register/', core.views.RegisterUser.as_view(), name='user_register'),
]

router = DefaultRouter()
router.register('tags', core.views.TagViewSet, basename='tag')
router.register('items', core.views.ItemViewSet, basename='item')
urlpatterns +=router.urls

