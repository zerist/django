from django.forms import widgets
from rest_framework import serializers
from django.contrib.auth.models import User
from snippets.models import Snippets, LANGUAGE_CHOICES, STYLE_CHOICES

class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippets
        fields = ('id', 'title', 'code', 'linenos', 'language', 'style', 'owner')

    owner = serializers.ReadOnlyField(source='owner.username')

class UserSerializer(serializers.ModelSerializer):
    snippets = serializers.PrimaryKeyRelatedField(many=True, queryset=Snippets.objects.all())

    class Meta:
        model = User
        fields = ('id', 'username', 'snippets')
