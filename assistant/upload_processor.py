from .models import Novel
from .models import Paragraph
import logging


def handle_uploaded_file(title, file):
    # todo change
    author_id = 1
    novel = Novel.objects.create_novel(title, author_id)
    content_type = file.content_type

    if (content_type != 'text/plain'):
        return -1

    data = file.read().decode("utf-8")


    paragraphs = data.splitlines()
    for paragraph in paragraphs:
        Paragraph.objects.create_paragraph(False, paragraph, novel.pk)
    file.close()
    print("Done")
