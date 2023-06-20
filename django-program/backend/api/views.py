from rest_framework import generics
from .models import Note
from .serializers import NoteSerializer

from .Faq import Faq
from .serializers import FaqSerializer


class NoteList(generics.ListCreateAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

class NoteDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Note.objects.all()
    serializer_class = NoteSerializer

class FaqList(generics.ListCreateAPIView):
    queryset = Faq.objects.all()
    serializer_class = FaqSerializer

class FaqDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Faq.objects.all()
    serializer_class = FaqSerializer    
