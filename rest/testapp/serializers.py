from rest_framework import serializers
from testapp.models import Word

class WordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Word

