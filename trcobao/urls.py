# Django

from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from django.conf import settings

# Local 
from pages.views import home_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_view),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
