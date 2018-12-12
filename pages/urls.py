

""" Pages Urls"""

# Django
from django.urls import path

# Local
from pages import views

urlpatterns = [

    path(
        route='',
        view= views.home,
        name='home'
    ),

    path(
        route='ingresar/',
        view=views.login_v,
        name='login'
    ),

    path(
        route='registrarse',
        view=views.signup_v,
        name='signup'
    )

]