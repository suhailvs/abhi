from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path,include
from insurance.views import home
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('insurance.urls', namespace='insurance')),
    path('home/',home, name="home"),
    path('accounts/', include('django.contrib.auth.urls')),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
