

from django.urls import path

from teachers import views

urlpatterns = [
    path(
        route='',
        view=views.getTeacher,
        name='teachers'
    ),
]