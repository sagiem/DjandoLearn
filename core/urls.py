from django.urls import path
import core.views

urlpatterns = [
    path('', core.views.Index.as_view()),
    path('persons', core.views.Person.as_view()),
    # path('person/<int:id>/', core.views.person),
]
