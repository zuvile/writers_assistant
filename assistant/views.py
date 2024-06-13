import logging

from .ai_chat import ChatApp
from .models import Novel, Character, Chapter, Paragraph, Scene, Portrait
from .novel_importer import NovelImporter
import codecs
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser
from .serializers import NovelSerializer, UploadSerializer, CharacterSerializer, CharacterPostSerializer, \
    CharacterChangeSerializer, ChapterSerializer, ParagraphSerializer, SceneSerializer, PortraitSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from rest_framework.viewsets import ViewSet
from django.shortcuts import get_object_or_404
from .portrait_creator import create_portrait
from django.http import FileResponse
from django.conf import settings
import os


class NovelListApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        # novels = Novel.objects.filter(author_id = request.user.id)
        novels = Novel.objects.all()
        serializer = NovelSerializer(novels, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class NovelDetailApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, novel_id):
        try:
            return Novel.objects.get(id=novel_id)
        except Novel.DoesNotExist:
            return None

    def get(self, request, novel_id, *args, **kwargs):
        novel_instance = self.get_object(novel_id)
        if not novel_instance:
            return Response(
                {"res": "Object with novel id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = NovelSerializer(novel_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, novel_id, *args, **kwargs):
        novel_instance = self.get_object(novel_id)
        if not novel_instance:
            return Response(
                {"res": "Object with novel id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        data = {
            'novel_name': request.data.get('novel_name'),
            'word_count': request.data.get('word_count'),
        }
        serializer = NovelSerializer(instance=novel_instance, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, novel_id, *args, **kwargs):
        #todo delete related chapters, scenes, paragraphs
        novel_instance = self.get_object(novel_id)
        if not novel_instance:
            return Response(
                {"res": "Object with novel id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        Novel.objects.delete_with_children(novel_instance.id)
        return Response(
            {"res": "Object deleted!"},
            status=status.HTTP_200_OK
        )


# ViewSets define the view behavior.
class UploadViewSet(ViewSet):
    serializer_class = UploadSerializer
    permission_classes = [permissions.IsAuthenticated]
    parser_classes = [MultiPartParser]

    def create(self, request):
        utf8_file = codecs.EncodedFile(request.FILES['file_uploaded'], "utf-8")
        novel_importer = NovelImporter()
        novel_id = novel_importer.import_novel(request.data['novel_title'], request.data['genre'], utf8_file)
        if (novel_id != -1):
            return Response(
                {"res": "File uploaded!"},
                status=status.HTTP_201_CREATED
            )
        else:
            return Response({"res": "Upload failed"}, status=status.HTTP_400_BAD_REQUEST)


class NovelListApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        # novels = Novel.objects.filter(author_id = request.user.id)
        novels = Novel.objects.all()
        serializer = NovelSerializer(novels, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ChapterListView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ChapterSerializer

    def get(self, request, novel_id, *args, **kwargs):
        queryset = Chapter.objects.prefetch_related('novel').filter(novel__id=novel_id)
        serializer = ChapterSerializer(queryset, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

class SceneListView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = SceneSerializer

    def get(self, request, chapter_id, *args, **kwargs):
        queryset = Scene.objects.prefetch_related('chapter').filter(chapter_id=chapter_id)
        serializer = SceneSerializer(queryset, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

class ParagraphListView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = ParagraphSerializer

    def get(self, request, chapter_id, scene_id, *args, **kwargs):
        try:
            scene = Scene.objects.get(id=scene_id, chapter_id=chapter_id)
        except Scene.DoesNotExist:
            return Response(status=status.HTTP_404_NOT_FOUND)

        queryset = Paragraph.objects.prefetch_related('scene').filter(scene_id=scene.pk)
        serializer = ParagraphSerializer(queryset, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

class CharacterListView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = CharacterSerializer

    def get_queryset(self):
        return Character.objects.all()

    def get(self, request, *args, **kwargs):
        #todo filter by novel
        queryset = Character.objects.prefetch_related('novels').all()
        serializer = CharacterSerializer(queryset, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args):
        data = {
            'name': request.data.get('name'),
            'age': request.data.get('age'),
            'gender': request.data.get('gender'),
            'description': request.data.get('description'),
            'novels': request.data.get('novels')
        }

        serializer = CharacterPostSerializer(data=data)
        if serializer.is_valid():
            character = serializer.save()
            create_portrait(character)
            return Response(serializer.data, status=status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CharacterDetailApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self, character_id):
        try:
            return Character.objects.get(id=character_id)
        except Character.DoesNotExist:
            return None

    def get(self, request, character_id, *args, **kwargs):
        character_instance = self.get_object(character_id)
        if not character_instance:
            return Response(
                {"res": "Object with novel id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )

        serializer = CharacterSerializer(character_instance)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, character_id, *args, **kwargs):
        character_instance = self.get_object(character_id)
        if not character_instance:
            return Response(
                {"res": "Object with character id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        data = {}

        if request.data.get('novels') is not None:
            data['novels'] = request.data.get('novels')
        if request.data.get('name') is not None:
            data['name'] = request.data.get('name')

        serializer = CharacterChangeSerializer(instance=character_instance, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def patch(self, request, character_id, *args, **kwargs):
        character_instance = self.get_object(character_id)
        if not character_instance:
            return Response(
                {"res": "Object with character id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        data = {}

        if request.data.get('name') is not None:
            data['name'] = request.data.get('name')

        if request.data.get('description') is not None:
            data['description'] = request.data.get('description')

        if request.data.get('age') is not None:
            data['age'] = request.data.get('age')

        serializer = CharacterChangeSerializer(instance=character_instance, data=data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, character_id, *args, **kwargs):
        character_instance = self.get_object(character_id)
        if not character_instance:
            return Response(
                {"res": "Object with novel id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        character_instance.delete()
        return Response(
            {"res": "Object deleted!"},
            status=status.HTTP_200_OK
        )


class CurrentPortraitApiView(APIView):
    #todo figure out authetication
    permission_classes = [permissions.AllowAny]
    #todo add test with static file
    def get(self, request, character_id, *args, **kwargs):
        character_instance = get_object_or_404(Character, pk=character_id)
        portrait = Portrait.objects.filter(character_id=character_instance.pk, active=True).first()

        if portrait:
            image_path = os.path.join(settings.BASE_DIR, 'assistant', 'static', portrait.url)
            logging.error(image_path)
            if os.path.exists(image_path):
                return FileResponse(open(image_path, 'rb'), content_type='image/jpeg')
            else:
                return Response({"error": "Image not found"}, status=status.HTTP_404_NOT_FOUND)
        else:
            return Response({"error": "Portrait not found for this character"}, status=status.HTTP_404_NOT_FOUND)


class PortraitListApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    def post(self, request, character_id, *args, **kwargs):
        character = get_object_or_404(Character, pk=character_id)
        previous_portraits = Portrait.objects.filter(character_id=character.pk).all()

        for portrait in previous_portraits:
            portrait.active = False
            portrait.save()

        portrait = create_portrait(character)
        serializer = PortraitSerializer(portrait)
        return Response(serializer.data, status=status.HTTP_200_OK)


class ChatApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        response = ChatApp().chat(request.data['message'])
        return Response(
            {"response": response},
            status=status.HTTP_200_OK
        )
