
# Django
from django.urls import path

# Local
from courses.views import coursesView, coursesViewId

urlpatterns = [
    path(
        route='',
        view=coursesView.as_view(),
        name='get'
    ),
    path(
        route='<int:id>/',
        view=coursesViewId.as_view(),
        name='delete'
    ),
]