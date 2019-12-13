import datetime
from django.db import models
from ckeditor_uploader.fields import RichTextUploadingField
from django.utils import timezone

class News(models.Model):
    title = models.CharField(max_length=50)
    text_news = RichTextUploadingField()
    author_text = models.CharField(max_length=50)
    pub_date = models.DateTimeField()
    is_public = models.BooleanField(default=False)

    def __str__(self):
        return self.title


class Comment(models.Model):
    news = models.ForeignKey(News, on_delete=models.CASCADE)
    comment_text = RichTextUploadingField()
    author_name = models.CharField(max_length=50)
    pub_date = models.DateTimeField()

    def __str__(self):
        return self.author_name