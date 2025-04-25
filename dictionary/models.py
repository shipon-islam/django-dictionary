from django.db import models
from django_quill.fields import QuillField
# Create your models here.
class Dictionary(models.Model):
    word = models.CharField(max_length=100, unique=True)
    summary = models.TextField()
    desccription =QuillField()

    def __str__(self):
        return self.word