from rest_framework import serializers
from .models import Post, Comment
from django.contrib.auth.models import User


class SearchFormSerializer(serializers.Serializer):
    query = serializers.CharField(max_length=100)

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
class CommentupdateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ["content"]

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ["username", "email", "password1", "password2"]


class PostSerializer(serializers.ModelSerializer):
    comments = CommentSerializer(many=True, read_only=True)
    
    class Meta:
        model = Post
        fields = '__all__'
