from rest_framework import serializers
from rest_framework.serializers import Serializer, FileField, CharField
from .models import Novel


class NovelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Novel
        fields = ["id", "novel_name", "upload_date", "author", "word_count"]


# Serializers define the API representation.
class UploadSerializer(Serializer):
    novel_title = CharField()
    file_uploaded = FileField()

    class Meta:
        fields = ['file_uploaded']
        novel_title = ['novel_title']