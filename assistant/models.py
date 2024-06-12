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
    def create_novel(self, title, genre, author_id):
        author = get_object_or_404(Author, pk=author_id)
        novel = self.create(novel_name=title, upload_date=timezone.now(), author_id=author.pk, word_count=0, genre=genre)
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
    genre = models.TextField(blank=True)
    objects = NovelManager()

    def __str__(self):
        return self.novel_name


class ParagraphManager(models.Manager):
    def create_paragraph(self, is_dialogue, text, novel_id, chapter_id, scene_id):
        novel = get_object_or_404(Novel, pk=novel_id)
        chapter = get_object_or_404(Chapter, pk=chapter_id)
        scene = get_object_or_404(Scene, pk=scene_id)
        paragraph = self.create(
            novel_id=novel.pk, is_dialogue=is_dialogue,
            text=text, chapter_id=chapter.pk, scene_id=scene.pk)
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


class CharacterManager(models.Manager):
    pass


class SceneManager(models.Manager):
    def create_scene(self, chapter_id, number):
        chapter = get_object_or_404(Chapter, pk=chapter_id)
        scene = self.create(chapter_id=chapter.pk, number=number)
        scene.save()

        return scene


class Chapter(models.Model):
    novel = models.ForeignKey(Novel, on_delete=models.CASCADE)
    number = models.IntegerField(default=0)
    word_count = models.IntegerField(default=0)
    title = models.TextField(blank=True)
    objects = ChapterManager()
    summary = models.TextField(blank=True)
    characters = models.ManyToManyField('Character')


class Scene(models.Model):
    chapter = models.ForeignKey(Chapter,  on_delete=models.CASCADE)
    number = models.IntegerField(default=1)
    objects = SceneManager()
    def __str__(self):
        return 'scene: ' + str(self.number)


class Paragraph(models.Model):
    is_dialogue = models.BooleanField(default=False)
    text = models.TextField(blank=True)
    novel = models.ForeignKey(Novel, on_delete=models.CASCADE)
    chapter = models.ForeignKey(Chapter, on_delete=models.CASCADE, null=True)
    scene = models.ForeignKey(Scene, on_delete=models.CASCADE, null=True)
    objects = ParagraphManager()


class Character(models.Model):
    name = models.TextField(max_length=300)
    novels = models.ManyToManyField(Novel)
    description = models.TextField(blank=True)
    age = models.IntegerField(default=0)
    gender = models.TextField(blank=True)
    objects = CharacterManager()


class Portrait(models.Model):
    character = models.ForeignKey(Character, on_delete=models.CASCADE)
    url = models.URLField(max_length=200)
    objects = models.Manager()
    active = models.BooleanField(default=True)