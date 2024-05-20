from django.urls import path

from . import views

app_name = "assistant"

urlpatterns = [
    path("", views.index, name="index"),
    path("novels/<int:novel_id>/", views.novel, name="novel"),
    path("upload", views.upload_novel, name="upload"),
    path("success", views.success, name="success")
]