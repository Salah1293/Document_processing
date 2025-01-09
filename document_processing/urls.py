
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('uploads.urls')),
    path('file_management/', include('file_management.urls')),
    path('operations/', include('operations.urls')),
]



urlpatterns += static(settings.MEDIA_URL , document_root=settings.MEDIA_ROOT)
