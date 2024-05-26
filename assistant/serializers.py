from rest_framework import serializers
from rest_framework.serializers import Serializer, FileField, CharField, IntegerField, PrimaryKeyRelatedField
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
    novels = PrimaryKeyRelatedField(many=True, queryset=Novel.objects.all())

    class Meta:
        model = Character
        fields = ["name", "novels"]

    def create(self, validated_data):
        logger = logging.getLogger('django')
        novels_data = validated_data.get('novels')
        logger.error(novels_data)
        character = Character.objects.create(name=validated_data.get('name'))
        character.save()
        for novel in novels_data:
            character.novels.add(novel)
        logging.error(character.novels)

        return character


class CharacterSerializer(serializers.ModelSerializer):
    novels = NovelSerializer(read_only=True, many=True)
    logging.error(novels)
    class Meta:
        model = Character
        fields = ["name", "novels"]


class CharacterPutSerializer(serializers.ModelSerializer):
    novels = PrimaryKeyRelatedField(many=True, queryset=Novel.objects.all(), allow_null=True)
    name = CharField(allow_null=True)

    class Meta:
        model = Character
        fields = ["name", "novels"]


class UploadSerializer(Serializer):
    novel_title = CharField()
    file_uploaded = FileField()

    class Meta:
        fields = ['file_uploaded']
        novel_title = ['novel_title']
