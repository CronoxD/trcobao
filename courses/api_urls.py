
# Django
from django.urls import path

# Local
from courses.views import coursesViewApi, coursesViewIdApi

urlpatterns = [
    path(
        route='',
        view=coursesViewApi.as_view(),
        name='get'
    ),
    path(
        route='<int:id>/',
        view=coursesViewIdApi.as_view(),
    ),
]