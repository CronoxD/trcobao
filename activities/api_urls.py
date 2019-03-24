
# Django
from django.urls import path

# Local
from activities.views import activitiesViewApi, activitiesViewIdApi

urlpatterns = [
    path(
        route='',
        view=activitiesViewApi.as_view(),
        name='get_acitivities'
    ),
    path(
        route='<int:id>/',
        view=activitiesViewIdApi.as_view(),
        name='delete_activity'
    )
    
]