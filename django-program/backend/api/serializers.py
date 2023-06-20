from rest_framework import serializers
from .models import Note
from .Faq import Faq

class NoteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Note
        fields = ('id', 'title', 'text', 'author', 'username', 'link', 'date_field')

class FaqSerializer(serializers.ModelSerializer):
    class Meta:
        model = Faq
        fields = ('id', 'subject', 'question', 'solution1', 'solution2', 'postedby')

