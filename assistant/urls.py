from django.urls import path, include
from rest_framework import routers

from . import views
from .views import (
    NovelListApiView,
    NovelDetailApiView,
    UploadViewSet,
)

app_name = "assistant"
router = routers.DefaultRouter()
router.register(r'api/novels/upload', UploadViewSet, basename="upload")

urlpatterns = [
    path('', include(router.urls)),
    path('api/novels/', NovelListApiView.as_view()),
    path('api/novels/<int:novel_id>/', NovelDetailApiView.as_view())
]