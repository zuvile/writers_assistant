import os
from .models import Author
from .models import Novel
from .models import Character
from .models import Paragraph
from .models import Scene
from .models import Chapter
from django.contrib.auth.models import User
from rest_framework.test import APITestCase
from .upload_processor import process_paragraphs
import json
from django.core.files.uploadedfile import SimpleUploadedFile
from rest_framework import status


class ApiTest(APITestCase):
    _novel_id = 0

    def setUp(self):
        User.objects.create_user('test_user', 'email', 'secret')
        self.assertTrue(self.client.login(username='test_user', password='secret'))
        f = open(os.path.join(os.getcwd(), "assistant", "samples", "book.txt"))
        data = f.read()
        paragraphs = data.splitlines()
        author = Author.objects.create_author('John Doe')
        novel = Novel.objects.create_novel('A New Novel', 'Fantasy', author.pk)
        self._novel_id = novel.pk
        process_paragraphs(paragraphs, novel.pk)

    def test_get_novel(self):
        response = self.client.get('/assistant/api/novels/' + str(self._novel_id) + '/')
        self.assertEquals(status.HTTP_200_OK, response.status_code)
        response_json = response.json()
        self.assertEquals(response_json['id'], 1)
        self.assertEquals(response_json['novel_name'], 'A New Novel')
        self.assertEquals(response_json['word_count'], 31)
        self.assertEquals(response_json['genre'], 'Fantasy')

    def test_get_novel_list(self):
        response = self.client.get('/assistant/api/novels/')
        self.assertEquals(status.HTTP_200_OK, response.status_code)
        response_json = response.json()
        self.assertEquals(response_json[0]['id'], 1)
        self.assertEquals(response_json[0]['novel_name'], 'A New Novel')
        self.assertEquals(response_json[0]['word_count'], 31)

    def test_put_novel(self):
        data = {
            'novel_name': 'Updated Novel Name',
            'word_count': 123
        }
        response = self.client.put('/assistant/api/novels/' + str(self._novel_id) + '/', data)
        self.assertEquals(status.HTTP_200_OK, response.status_code)
        response_json = response.json()
        self.assertEquals(response_json['novel_name'], 'Updated Novel Name')
        self.assertEquals(response_json['word_count'], 123)

    def test_delete_novel(self):
        response = self.client.delete('/assistant/api/novels/' + str(self._novel_id) + '/')
        self.assertEquals(status.HTTP_200_OK, response.status_code)

    def test_get_character_list(self):
        character = Character.objects.create(name="John")
        response = self.client.get('/assistant/api/novels/characters/')
        self.assertEquals(status.HTTP_200_OK, response.status_code)
        response_json = response.json()
        self.assertEquals(response_json[0]['name'], 'John')

    def test_get_character(self):
        character = Character.objects.create(name="John")
        response = self.client.get('/assistant/api/novels/characters/' + str(character.pk) + '/')
        self.assertEquals(status.HTTP_200_OK, response.status_code)
        response_json = response.json()
        self.assertEquals(response_json['name'], 'John')

    def test_post_character(self):
        response = self.client.post('/assistant/api/novels/characters/', json.dumps({
            "name": "James",
            "novels": [self._novel_id],
            "age": 25,
            "description": "Blond hair and brown eyes"
        }), content_type='application/json')
        self.assertEquals(status.HTTP_201_CREATED, response.status_code)
        response_json = response.json()
        self.assertEquals(response_json['name'], 'James')
        self.assertEquals(response_json['novels'], [self._novel_id])
        self.assertEquals(response_json['age'], 25)
        self.assertEquals(response_json['description'], "Blond hair and brown eyes")
        character = Character.objects.get(name='James')
        self.assertIsNotNone(character)
        novel = Novel.objects.get(id=self._novel_id)
        self.assertEquals(novel, character.novels.get(pk=novel.pk))

    def test_delete_character(self):
        author = Author.objects.create_author('John Doe')
        novel = Novel.objects.create_novel('A New Novel', 'Fantasy', author.pk)
        response = self.client.post('/assistant/api/novels/characters/', json.dumps({
            "name": "Patrick",
            "age": 25,
            "description": "Tall",
            "novels": [novel.pk]
        }), content_type='application/json')
        self.assertEquals(status.HTTP_201_CREATED, response.status_code)
        character = Character.objects.get(name='Patrick')
        self.assertIsNotNone(character)
        response = self.client.delete('/assistant/api/novels/characters/' + str(character.id) + '/')
        self.assertEquals(200, response.status_code)
        with self.assertRaises(Character.DoesNotExist):
            Character.objects.get(pk=character.pk)

    def test_put_character(self):
        author = Author.objects.create_author('John Doe')
        novel = Novel.objects.create_novel('A New Novel', 'Fantasy', author.pk)
        response = self.client.post('/assistant/api/novels/characters/', json.dumps({
            "name": "Patrick",
            "novels": [novel.pk],
            "age": 20,
            "description": "Short"
        }), content_type='application/json')
        self.assertEquals(status.HTTP_201_CREATED, response.status_code)
        character = Character.objects.get(name="Patrick")
        response = self.client.put('/assistant/api/novels/characters/' + str(character.id) + '/', json.dumps({
            "name": "Patrick2"
        }), content_type='application/json')
        self.assertEquals(status.HTTP_200_OK, response.status_code)
        character = Character.objects.get(name="Patrick2")
        self.assertIsNotNone(character)

    def test_get_chapters(self):
        response = self.client.get('/assistant/api/novels/' + str(self._novel_id) + '/chapters/')
        self.assertEquals(status.HTTP_200_OK, response.status_code)
        response_json = response.json()
        self.assertEquals(response_json[1]['id'], 2)
        self.assertEquals(response_json[1]['number'], 1)
        self.assertEquals(response_json[1]['title'], 'The beginning')
        self.assertEquals(response_json[1]['word_count'], 13)

    def test_get_scenes(self):
        response = self.client.get('/assistant/api/novels/' + str(self._novel_id) + '/chapters/1/scenes/')
        self.assertEquals(status.HTTP_200_OK, response.status_code)
        response_json = response.json()
        self.assertEquals(response_json[0]['id'], 1)
        self.assertEquals(response_json[0]['number'], 1)

    def test_get_paragraphs(self):
        chapter_id = Chapter.objects.get(novel_id=self._novel_id, title='The beginning').pk
        response = self.client.get(
            '/assistant/api/novels/' + str(
                self._novel_id) + '/chapters/' + str(chapter_id) + '/scenes/3/paragraphs/')
        self.assertEquals(status.HTTP_200_OK, response.status_code)
        response_json = response.json()
        self.assertEquals(response_json[0]['text'], 'This is scene 2.')

    def test_get_paragraphs_on_invalid_scene(self):
        response = self.client.get('/assistant/api/novels/' + str(self._novel_id) + '/chapters/1/scenes/3/paragraphs/')
        self.assertEquals(status.HTTP_404_NOT_FOUND, response.status_code)

    def test_upload_novel(self):
        file_content = b'''
Prologue
Some text
1. Chapter one
Scene 1
***
Scene 2
2. Chapter two
More text
        '''
        file = SimpleUploadedFile('test_novel.txt', file_content, content_type='text/plain')
        data = {
            'novel_title': 'Test Novel',
            'genre': 'Fantasy',
            'file_uploaded': file
        }
        response = self.client.post('/assistant/api/novels/upload/', data, format='multipart')

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        novel = Novel.objects.get(novel_name='Test Novel')
        self.assertIsNotNone(novel)
        self.assertEquals(18, novel.word_count)
        paragraphs = Paragraph.objects.filter(novel_id=novel.pk)
        chapters = Chapter.objects.filter(novel_id=novel.pk)
        self.assertEquals(6, len(paragraphs))
        self.assertEquals(3, len(chapters))

        chapter1_scenes = Scene.objects.filter(chapter_id=chapters[1].pk)
        self.assertEquals(2, len(chapter1_scenes))
        chapter2_scenes = Scene.objects.filter(chapter_id=chapters[2].pk)
        self.assertEquals(1, len(chapter2_scenes))