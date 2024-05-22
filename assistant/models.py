from django.db import models
from django.utils import timezone
from django.shortcuts import get_object_or_404


class AuthorManager(models.Manager):
    def create_author(self, name):
        author = self.create(name=name)
        return author


class Author(models.Model):
    name = models.CharField(max_length=200)
    objects = AuthorManager()

    def __str__(self):
        return self.name

class NovelManager(models.Manager):
    def create_novel(self, title, author_id):
        author = get_object_or_404(Author, pk=author_id)
        novel = self.create(novel_name=title, upload_date=timezone.now(), author_id=author.pk)
        return novel

    def update_word_count(self, novel_id, word_count):
        novel = Novel.objects.get(pk=novel_id)
        novel.word_count = word_count
        novel.save()


class Novel(models.Model):
    novel_name = models.CharField(max_length=200)
    upload_date = models.DateTimeField("date uploaded")
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    word_count = models.IntegerField(default=0)
    objects = NovelManager()

    def __str__(self):
        return self.novel_name


class ParagraphManager(models.Manager):
    def create_paragraph(self, is_dialogue, text, novel_id, chapter_id):
        novel = get_object_or_404(Novel, pk=novel_id)
        paragraph = self.create(novel_id=novel.pk, is_dialogue=is_dialogue, text=text, chapter_id=chapter_id)
        return paragraph


class ChapterManager(models.Manager):
    def create_chapter(self, novel_id, number, word_count, title):
        novel = get_object_or_404(Novel, pk=novel_id)
        chapter = self.create(novel_id=novel.pk, number=number,
                              word_count=word_count,
                              title=title)
        return chapter

    def update_word_count(self, chapter_id, word_count):
        chapter = Chapter.objects.get(pk=chapter_id)
        chapter.word_count = word_count
        chapter.save()


class Chapter(models.Model):
    novel = models.ForeignKey(Novel, on_delete=models.CASCADE)
    number = models.IntegerField(default=0)
    word_count = models.IntegerField(default=0)
    title = models.TextField(blank=True)
    objects = ChapterManager()


class Paragraph(models.Model):
    is_dialogue = models.BooleanField(default=False)
    text = models.TextField(blank=True)
    novel = models.ForeignKey(Novel, on_delete=models.CASCADE)
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE, null=True)
    objects = ParagraphManager()