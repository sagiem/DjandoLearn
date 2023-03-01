from django.urls import path
from rest_framework.routers import DefaultRouter
import core.views

urlpatterns = [
    path('', core.views.Index.as_view()),
    path('persons', core.views.Person.as_view()),
    # path('tags', core.views.Tags.as_view()),
    # path('tags/<pk>/', core.views.Tag.as_view()),
    path('person/<int:id>/', core.views.person),
]

router = DefaultRouter()
router.register('tags', core.views.TagViewSet, basename="tag")
urlpatterns +=router.urls

