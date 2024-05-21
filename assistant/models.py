from django.db import models
from django.utils import timezone
from django.shortcuts import get_object_or_404
import datetime


class Author(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name


class NovelManager(models.Manager):
    def create_novel(self, title, author_id):
        author = get_object_or_404(Author, pk=author_id)
        novel = self.create(novel_name=title, upload_date=timezone.now(), author_id=author.pk)
        return novel


class Novel(models.Model):
    novel_name = models.CharField(max_length=200)
    upload_date = models.DateTimeField("date uploaded")
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    objects = NovelManager()

    def __str__(self):
        return self.novel_name

    def was_uploaded_recently(self):
        return self.upload_date >= timezone.now() - datetime.timedelta(days=1)


class ParagraphManager(models.Manager):
    def create_paragraph(self, is_dialogue, text, novel_id):
        novel = get_object_or_404(Novel, pk=novel_id)
        paragraph = self.create(novel_id=novel.pk, is_dialogue=is_dialogue, text=text)
        return paragraph


class Paragraph(models.Model):
    is_dialogue = models.BooleanField(default=False)
    text = models.TextField(blank=True)
    novel = models.ForeignKey(Novel, on_delete=models.CASCADE)
    objects = ParagraphManager()