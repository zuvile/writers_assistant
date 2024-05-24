from .models import Novel
from .models import Paragraph
from .models import Chapter
import re

_exclude_from_wordcount = ['–', '?', ',']


def handle_uploaded_file(title, file):
    # todo change
    author_id = 1

    content_type = file.content_type

    if (content_type != 'text/plain'):
        return -1

    novel = Novel.objects.create_novel(title, author_id)
    data = file.read().decode("utf-8")
    process_paragraphs(data.splitlines(), novel.pk)
    file.close()

    return novel.pk


def process_paragraphs(paragraphs, novel_id):
    chapter_word_count = 0
    novel_word_count = 0

    #initial chapter. This could be a prologue or something else
    current_chapter = Chapter.objects.create_chapter(novel_id, -1, 0, 'Prologue')
    for paragraph in paragraphs:
        # skip new line
        if (paragraph == '\n' or paragraph == ''):
            continue
        number, title = get_chapter(paragraph)
        if (number):
            #update previous chapter
            Chapter.objects.update_word_count(current_chapter.pk, chapter_word_count)
            #create new chapter
            current_chapter = Chapter.objects.create_chapter(novel_id, number, 0, title)
            chapter_word_count = 0
        else:
            #paragraph is normal
            word_count = get_real_word_count(paragraph.split(' '))
            chapter_word_count += word_count
            novel_word_count += word_count
            is_dialogue = dialogue(paragraph)
            Paragraph.objects.create_paragraph(is_dialogue, paragraph, novel_id, current_chapter.pk)
    # update final chapter and novel word counts
    Chapter.objects.update_word_count(current_chapter.pk, chapter_word_count)
    Novel.objects.update_word_count(novel_id, novel_word_count)


def get_chapter(paragraph):
    chapter_title = re.search('(^\d+).(.*)', paragraph)
    if (chapter_title):
        number = chapter_title.group(1).strip()
        title = chapter_title.group(2).strip()
        return number, title
    else:
        return False, False


def get_real_word_count(words):
    count = 0
    for word in words:
        if word not in _exclude_from_wordcount:
            count = count + 1
    return count


def dialogue(paragraph):
    return paragraph.startswith('–')
