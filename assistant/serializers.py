from rest_framework import serializers
from rest_framework.serializers import Serializer, FileField, CharField, IntegerField, PrimaryKeyRelatedField, \
    BooleanField
from .models import Novel, Character, Paragraph, Chapter, Scene, Portrait


class NovelSerializer(serializers.ModelSerializer):
    class Meta:
        model = Novel
        fields = ["id", "novel_name", "genre", "upload_date", "author", "word_count"]


class NovelIdSerializer(serializers.ModelSerializer):
    id = IntegerField()
    fields = ["id"]


class CharacterPostSerializer(Serializer):
    name = CharField()
    novels = PrimaryKeyRelatedField(many=True, queryset=Novel.objects.all())
    age = IntegerField()
    description = CharField()

    class Meta:
        model = Character
        fields = ["name", "age", "description", "gender", "novels"]

    def create(self, validated_data):
        novels_data = validated_data.get('novels')
        character = Character.objects.create(name=validated_data.get('name'),
                                             description=validated_data.get('description'),
                                             age=validated_data.get('age'))
        character.save()
        for novel in novels_data:
            character.novels.add(novel)

        return character


class CharacterSerializer(serializers.ModelSerializer):
    novels = NovelSerializer(read_only=True, many=True)

    class Meta:
        model = Character
        fields = ["id", "name", "age", "description", "gender", "novels"]

class CharacterBasicSerializer(serializers.ModelSerializer):
    class Meta:
        model = Character
        fields = ["id", "name", "age", "description", "gender"]

class PortraitSerializer(serializers.ModelSerializer):
    class Meta:
        model = Portrait
        fields = ["url", "active"]

class ParagraphSerializer(serializers.ModelSerializer):
    class Meta:
        model = Paragraph
        fields = ["text"]


class ChapterSerializer(serializers.ModelSerializer):
    characters = CharacterBasicSerializer(read_only=True, many=True)
    class Meta:
        model = Chapter
        fields = ["id", "number", "title", "word_count", "characters", "summary"]


class SceneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scene
        fields = ["id", "number"]


class CharacterPutSerializer(serializers.ModelSerializer):
    novels = PrimaryKeyRelatedField(many=True, queryset=Novel.objects.all(), allow_null=True)
    name = CharField(allow_null=True)

    class Meta:
        model = Character
        fields = ["name", "novels"]


class UploadSerializer(Serializer):
    novel_title = CharField()
    file_uploaded = FileField()
    genre = CharField()

    class Meta:
        fields = ['file_uploaded']
        novel_title = ['novel_title']
