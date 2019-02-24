# Django

from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [

    path('admin/', admin.site.urls),
    path('', include(('access_auth.urls', 'access_auth'), namespace='access_auth')),
    path('maestros/', include(('teachers.urls', 'teachers'), namespace='teachers')),
    #path('courses/', include(('courses.urls', 'courses'), namespace='courses')),
    path('api/courses/', include(('courses.api_urls', 'api_courses'), namespace='api_courses')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
