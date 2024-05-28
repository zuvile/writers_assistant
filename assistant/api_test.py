import os
from .models import Author
from .models import Novel
from .models import Chapter
from .models import Paragraph
from .models import Scene
from .models import Character
from django.contrib.auth.models import User
from rest_framework.test import force_authenticate
from rest_framework.test import APIClient, APITestCase
from .upload_processor import process_paragraphs
from django.urls import reverse
import json


class ApiTest(APITestCase):
    _novel_id = 0

    def setUp(self):
        User.objects.create_user('test_user', 'email', 'secret')
        self.assertTrue(self.client.login(username='test_user', password='secret'))
        f = open(os.path.join(os.getcwd(), "assistant", "samples", "book.txt"))
        data = f.read()
        paragraphs = data.splitlines()
        author = Author.objects.create_author('John Doe')
        novel = Novel.objects.create_novel('A New Novel', author.pk)
        self._novel_id = novel.pk
        process_paragraphs(paragraphs, novel.pk)

    def test_get_novel(self):
        response = self.client.get('/assistant/api/novels/' + str(self._novel_id) + '/')
        self.assertEquals(200, response.status_code)
        response_json = response.json()
        self.assertEquals(response_json['id'], 1)
        self.assertEquals(response_json['novel_name'], 'A New Novel')
        self.assertEquals(response_json['word_count'], 31)

    def test_get_novel_list(self):
        response = self.client.get('/assistant/api/novels/')
        self.assertEquals(200, response.status_code)
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
        self.assertEquals(200, response.status_code)
        response_json = response.json()
        self.assertEquals(response_json['novel_name'], 'Updated Novel Name')
        self.assertEquals(response_json['word_count'], 123)

    def test_delete_novel(self):
        response = self.client.delete('/assistant/api/novels/' + str(self._novel_id) + '/')
        self.assertEquals(200, response.status_code)


    def test_get_character_list(self):
        character = Character.objects.create(name="John")
        response = self.client.get('/assistant/api/novels/characters/')
        self.assertEquals(200, response.status_code)
        response_json = response.json()
        self.assertEquals(response_json[0]['name'], 'John')

    def test_get_character(self):
        character = Character.objects.create(name="John")
        response = self.client.get('/assistant/api/novels/characters/' + str(character.pk) + '/')
        self.assertEquals(200, response.status_code)
        response_json = response.json()
        self.assertEquals(response_json['name'], 'John')

    def test_post_character(self):
        response = self.client.post('/assistant/api/novels/characters/', json.dumps({
            "name": "James",
            "novels": [self._novel_id]
        }), content_type='application/json')
        self.assertEquals(201, response.status_code)
        response_json = response.json()
        self.assertEquals(response_json['name'], 'James')
        self.assertEquals(response_json['novels'], [self._novel_id])
        character = Character.objects.get(name='James')
        self.assertIsNotNone(character)
        novel = Novel.objects.get(id=self._novel_id)
        self.assertEquals(novel, character.novels.get(pk=novel.pk))


    def test_delete_character(self):
        author = Author.objects.create_author('John Doe')
        novel = Novel.objects.create_novel('A New Novel', author.pk)
        response = self.client.post('/assistant/api/novels/characters/', json.dumps({
            "name": "Patrick",
            "novels": [novel.pk]
        }), content_type='application/json')
        self.assertEquals(201, response.status_code)
        character = Character.objects.get(name='Patrick')
        self.assertIsNotNone(character)
        response = self.client.delete('/assistant/api/novels/characters/' + str(character.id) + '/')
        self.assertEquals(200, response.status_code)
        with self.assertRaises(Character.DoesNotExist):
            Character.objects.get(pk=character.pk)


    def test_put_character(self):
        author = Author.objects.create_author('John Doe')
        novel = Novel.objects.create_novel('A New Novel', author.pk)
        response = self.client.post('/assistant/api/novels/characters/', json.dumps({
            "name": "Patrick",
            "novels": [novel.pk]
        }), content_type='application/json')
        self.assertEquals(201, response.status_code)
        character = Character.objects.get(name="Patrick")
        response = self.client.put('/assistant/api/novels/characters/' + str(character.id) + '/', json.dumps({
            "name": "Patrick2"
        }), content_type='application/json')
        self.assertEquals(200, response.status_code)
        character = Character.objects.get(name="Patrick2")
        self.assertIsNotNone(character)
