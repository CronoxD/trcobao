

""" Auth Urls"""

# Django
from django.urls import path

# Local
from access_auth import views

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
        route='registrarse/',
        view=views.signup_v,
        name='signup'
    ),

    path(
        route='logout/',
        view=views.logout_v,
        name='logout'
    )

]