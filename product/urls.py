from django.contrib import admin
from django.urls import path
from .views import home
from django.conf import settings
from django.conf.urls.static import static

app_name = "product"
urlpatterns = [
    path("",home, name="home"),
]
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)