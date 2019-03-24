# Django

from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [

    path('admin/', admin.site.urls),
    path('auth/', include(('access_auth.urls', 'access_auth'), namespace='access_auth')),
    path('api/courses/', include(('courses.api_urls', 'api_courses'), namespace='api_courses')),
    path('api/activities/', include(('activities.api_urls', 'api_activities'), namespace='api_activities')),

    #Español
    path('api/grupos/', include(('courses.api_urls', 'api_courses'), namespace='api_grupos')),
    path('api/actividades/', include(('activities.api_urls', 'api_activities'), namespace='api_actividades')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
