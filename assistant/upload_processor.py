from .models import Novel

class UploadProcessor:
    print("Processing file")
    def handle_uploaded_file(self, title, f):
        # todo change
        author_id = 1
        novel = Novel.objects.create_novel(title, 1)


