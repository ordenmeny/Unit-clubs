from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from project_clubs import settings

urlpatterns = [
    path('ckeditor5/', include('django_ckeditor_5.urls')),

    path('admin/', admin.site.urls),
    path('users/', include('users.urls'), name='users'),
    path('', include('app_clubs.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
