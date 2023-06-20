from rest_framework import serializers
from .models import *


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ['id', 'name', 'url']


class NewsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'author', 'post_type', 'time_creation', 'post_category', 'title', 'text', 'url']


class ArtsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id', 'author', 'post_type', 'time_creation', 'post_category', 'title', 'text', 'url']
