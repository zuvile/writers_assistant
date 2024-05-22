import os

from django.test import TestCase
from .upload_processor import process_paragraphs, get_chapter, get_real_word_count
from .models import Author
from .models import Novel
from .models import Chapter
from .models import Paragraph


class UploadProcessorTest(TestCase):
    def setUp(self):
        author = Author.objects.create_author('Sample author')
        Novel.objects.create_novel('Sample novel', author.pk)
        f = open(os.path.join(os.getcwd(), "assistant", "samples", "book.txt"))
        data = f.read()
        self._paragraphs = data.splitlines()

    def test_get_chapter_when_exists(self):
        paragraph = "1. The beginning"
        number, title = get_chapter(paragraph)
        self.assertEquals('1', number)
        self.assertEquals('The beginning', title)

    def test_get_chapter_when_no_exists(self):
        paragraph = "Some text"
        number, title = get_chapter(paragraph)
        self.assertFalse(number)
        self.assertFalse(title)

    def test_number_of_chapters(self):
        novel = Novel.objects.get(novel_name='Sample novel')
        process_paragraphs(self._paragraphs, novel.pk)
        chapters = Chapter.objects.all()
        self.assertEquals(4, len(chapters))

    def test_chapter_title(self):
        novel = Novel.objects.get(novel_name='Sample novel')
        process_paragraphs(self._paragraphs, novel.pk)
        chapter = Chapter.objects.get(title="The beginning")
        self.assertIsNotNone(chapter)

    def test_chapter_word_count(self):
        novel = Novel.objects.get(novel_name='Sample novel')
        process_paragraphs(self._paragraphs, novel.pk)
        chapter = Chapter.objects.get(title="Second Chapter")
        self.assertEquals(4, chapter.word_count)

    def test_chapter_word_count_with_dialogue(self):
        novel = Novel.objects.get(novel_name='Sample novel')
        process_paragraphs(self._paragraphs, novel.pk)
        chapter = Chapter.objects.get(title="The beginning")
        self.assertEquals(7, chapter.word_count)

    def test_get_real_word_count(self):
        paragraph = "– Hello, – he said."
        self.assertEquals(3, get_real_word_count(paragraph.split(' ')))

    def test_novel_word_count(self):
        novel = Novel.objects.get(novel_name='Sample novel')
        process_paragraphs(self._paragraphs, novel.pk)
        novel.refresh_from_db()
        self.assertEquals(25, novel.word_count)

    def test_number_in_middle_sentence_not_chapter_title(self):
        paragraph = "Something 223. and other"
        number, title = get_chapter(paragraph)
        self.assertFalse(number)
        self.assertFalse(title)

    def test_last_chapter_word_count(self):
        novel = Novel.objects.get(novel_name='Sample novel')
        process_paragraphs(self._paragraphs, novel.pk)
        chapter = Chapter.objects.get(title="This is the last chapter")
        self.assertEquals(8, chapter.word_count)

    def test_prologue(self):
        novel = Novel.objects.get(novel_name='Sample novel')
        process_paragraphs(self._paragraphs, novel.pk)
        chapter = Chapter.objects.get(number=-1)
        self.assertEquals(6, chapter.word_count)

    def test_chapter_paragraphs(self):
        novel = Novel.objects.get(novel_name='Sample novel')
        process_paragraphs(self._paragraphs, novel.pk)
        chapter = Chapter.objects.get(title="The beginning")
        paragraphs = Paragraph.objects.filter(chapter_id=chapter.pk)
        self.assertEquals(2, len(paragraphs))