from django.db import models
from django.utils import timezone
import datetime

class Author(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

class Novel(models.Model):
    novel_name = models.CharField(max_length=200)
    upload_date = models.DateTimeField("date uploaded")
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.novel_name
    def was_uploaded_recently(self):
        return self.upload_date >= timezone.now() - datetime.timedelta(days=1)
