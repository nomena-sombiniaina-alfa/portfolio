from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from informations.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home, name="home"),
    path('informations/', include('informations.urls')),
]
urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
