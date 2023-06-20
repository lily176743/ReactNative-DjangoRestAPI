from django.db import models
from django.utils import timezone


class Faq(models.Model):
    subject = models.CharField(max_length=100)
    question = models.TextField()
    solution1 = models.TextField(default='none')
    solution2 = models.TextField(default='none')
    postedby = models.CharField(max_length=100, default='admin')

    def __str__(self):
        return self.subject
