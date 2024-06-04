from django.urls import path, include
from rest_framework import routers

from . import views
from .views import (
    NovelListApiView,
    NovelDetailApiView,
    UploadViewSet,
    CharacterListView,
    CharacterDetailApiView,
    SearchViewSet,
    ChapterListView,
    ParagraphListView
)

app_name = "assistant"
router = routers.DefaultRouter()
router.register(r'api/novels/upload', UploadViewSet, basename="upload")
router.register(r'api/novels/search', SearchViewSet, basename="search")

urlpatterns = [
    path('', include(router.urls)),
    path('api/novels/', NovelListApiView.as_view()),
    path('api/novels/<int:novel_id>/', NovelDetailApiView.as_view()),
    path('api/novels/<int:novel_id>/chapters/', ChapterListView.as_view()),
    path('api/novels/<int:novel_id>/chapters/<chapter_id>/paragraphs/', ParagraphListView.as_view()),
    path('api/novels/characters/', CharacterListView.as_view()),
    path('api/novels/characters/<int:character_id>/', CharacterDetailApiView.as_view())
]