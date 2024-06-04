from .models import Novel, Character
from .upload_processor import handle_uploaded_file
from .character_search import search
import codecs
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser
from .serializers import NovelSerializer, UploadSerializer, CharacterSerializer, CharacterPostSerializer, CharacterPutSerializer
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from rest_framework.viewsets import ViewSet


class NovelListApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        # novels = Novel.objects.filter(author_id = request.user.id)
        novels = Novel.objects.all()
        serializer = NovelSerializer(novels, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)


class NovelDetailApiView(APIView):
    # add permission to check if user is authenticated
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
        novel_instance = self.get_object(novel_id)
        if not novel_instance:
            return Response(
                {"res": "Object with novel id does not exists"},
                status=status.HTTP_400_BAD_REQUEST
            )
        novel_instance.delete()
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
        novel_id = handle_uploaded_file(request.data['novel_title'], utf8_file)
        if (novel_id != -1):
            return Response(
                {"res": "File uploaded!"},
                status=status.HTTP_201_CREATED
            )
        else:
            return Response({"res": "Upload failed"}, status=status.HTTP_400_BAD_REQUEST)

class SearchViewSet(ViewSet):
    permission_classes = [permissions.IsAuthenticated]

    def list(self, request):
        search_term = request.query_params.get('term', '')
        novels = request.query_params.getlist('novels', '')
        results = search(search_term, novels)
        return Response(
            {"res": results},
            status=status.HTTP_200_OK
        )


class NovelListApiView(APIView):
    permission_classes = [permissions.IsAuthenticated]

    def get(self, request, *args, **kwargs):
        # novels = Novel.objects.filter(author_id = request.user.id)
        novels = Novel.objects.all()
        serializer = NovelSerializer(novels, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

class CharacterListView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    serializer_class = CharacterSerializer

    def get_queryset(self):
        return Character.objects.all()

    def get(self, request, *args, **kwargs):
        queryset = Character.objects.prefetch_related('novels').all()
        serializer = CharacterSerializer(queryset, many=True)

        return Response(serializer.data, status=status.HTTP_200_OK)


    def post(self, request, *args, **kwargs):
        data = {
            'name': request.data.get('name'),
            'novels': request.data.get('novels')
        }

        serializer = CharacterPostSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
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

        serializer = CharacterPutSerializer(instance=character_instance, data=data, partial=True)
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
