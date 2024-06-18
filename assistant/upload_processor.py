from .models import Novel
from .txt_processor import process_txt
from .word_processor import process_word
import codecs
import tempfile
import os

_exclude_from_wordcount = ['–', '?', ',', '***']


def handle_uploaded_file(title, genre, file):
    # todo change
    author_id = 1

    utf8_file = codecs.EncodedFile(file, "utf-8")
    content_type = file.content_type

    if content_type != 'text/plain' and content_type != 'application/vnd.openxmlformats-officedocument.wordprocessingml.document':
        return -1

    novel = Novel.objects.create_novel(title, genre, author_id)

    if content_type == 'text/plain':
        process_txt(utf8_file, novel.pk)
    if content_type == 'application/vnd.openxmlformats-officedocument.wordprocessingml.document':
        tmp_dir = tempfile.mkdtemp()
        tmp_file = os.path.join(tmp_dir, 'tmp.docx')
        with open(tmp_file, 'wb') as f:
            f.write(file.read())
        process_word(tmp_file, novel.pk)

    return novel.pk