from django.urls import path
import core.views

urlpatterns = [
    path('', core.views.Index.as_view()),
    path('persons', core.views.Person.as_view()),
    path('tags', core.views.tags),
    path('person/<int:id>/', core.views.person),
]
