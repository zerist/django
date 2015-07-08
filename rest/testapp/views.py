from django.shortcuts import render
from rest_framework import generics, views
from testapp.serializers import WordSerializer
from testapp.models import Word

# Create your views here.

class WordList(generics.ListCreateAPIView):
    queryset = Word.objects.all()
    serializer_class = WordSerializer
