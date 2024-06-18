from .upload_processor import handle_uploaded_file
from .novel_digestor import NovelDigestor

class NovelImporter():
    def import_novel(self, title, genre, file):
        novel_id = handle_uploaded_file(title, genre, file)
        if (novel_id == -1):
            return -1
        digestor = NovelDigestor()
        digestor.summarise(novel_id)

        return novel_id
