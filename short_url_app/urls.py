from django.urls import path
# from django.contrib import admin
from . import views

# Pre-Deployment Media Storage recommendations
from django.conf import settings
from django.conf.urls.static import static

app_name = "short_url_app"

urlpatterns = [
    path("", views.index, name="index"),
    path("expand/", views.url_expand, name="expand"),
    # Redirect to URL based on generated alpha-numeric pattern.
    path("<str:url_suffix>/", views.url_redirect, name="url_redirect")
] 

# Pre-Deployment check to see if currently in DEBUG mode
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)