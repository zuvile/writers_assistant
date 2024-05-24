from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from assistant.views import UploadViewSet

router = routers.DefaultRouter()
router.register(r'upload', UploadViewSet, basename="upload")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("assistant/", include("assistant.urls")),
    path('api-auth/', include('rest_framework.urls')),
]
