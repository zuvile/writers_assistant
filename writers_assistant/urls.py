from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("assistant/", include("assistant.urls")),
    path("admin/", admin.site.urls),
]