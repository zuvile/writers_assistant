from rest_framework import serializers
from rest_framework.serializers import Serializer, FileField, CharField, IntegerField, ListField
from .models import Novel, Character
import logging, json


class NovelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Novel
        fields = ["id", "novel_name", "upload_date", "author", "word_count"]

class NovelIdSerializer(serializers.ModelSerializer):
    id = IntegerField()
    fields = ["id"]

class CharacterPostSerializer(Serializer):
    name = CharField()
    novels = ListField()
    logging.error(novels)
    def create(self, validated_data):
        logger = logging.getLogger('django')
        novels_data = validated_data.get('novels')
        logger.error(novels_data)
        character = Character.objects.create(name=validated_data.get('name'))
        character.save()
        for novel in novels_data:
            logger.error("here")
            character.novels.add(Novel.objects.get(id=novel['id']))

        logger.error(character.novels)

        return character


class CharacterSerializer(serializers.ModelSerializer):
    novels = NovelSerializer(read_only=True, many=True)
    logging.error(novels)
    class Meta:
        model = Character
        fields = ["name", "novels"]


# Serializers define the API representation.
class UploadSerializer(Serializer):
    novel_title = CharField()
    file_uploaded = FileField()

    class Meta:
        fields = ['file_uploaded']
        novel_title = ['novel_title']
