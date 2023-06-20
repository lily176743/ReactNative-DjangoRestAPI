from django.db import models
from django.utils import timezone

class Note(models.Model):
    title = models.CharField(max_length=100)
    text = models.TextField()
    author = models.CharField(max_length=100, default='joel wembo')
    username = models.CharField(max_length=100, default='joelwembo')
    link = models.CharField(max_length=100, default='https:google.com')
    date_field = models.DateField(default=timezone.now, max_length=150)

    def __str__(self):
        return self.title
