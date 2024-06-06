from django_elasticsearch_dsl import Document, fields
from django_elasticsearch_dsl.registries import registry
from .models import Paragraph, Novel, Chapter
from django.db import models

#
# @registry.register_document
class ParagraphDocument(Document):
    novel = fields.ObjectField(properties={
        'novel_name': fields.TextField(),
    })
    chapter = fields.ObjectField(properties={
        'title': fields.TextField(),
        'number': fields.IntegerField(),
    })

    class Index:
        name = 'paragraphs'
        settings = {'number_of_shards': 2,
                    'number_of_replicas': 1}

    class Django:
        model = Paragraph
        fields = [
            'id',
            'is_dialogue',
            'text',
        ]
