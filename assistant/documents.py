# from django_elasticsearch_dsl import Document, fields
# from django_elasticsearch_dsl.registries import registry
# from .models import Paragraph
# from .models import Author
#
# @registry.register_document
# class ParagraphDocument(Document):
#
#
#     class Index:
#         name = 'paragraphs'
#         settings = {'number_of_shards': 2,
#                     'number_of_replicas': 1}
#
#     class Django:
#         model = Paragraph # The model associated with this Document
#         novel_id = fields.TextField()
#
#         fields = [
#             'id',
#             'is_dialogue',
#             'text',
#         ]