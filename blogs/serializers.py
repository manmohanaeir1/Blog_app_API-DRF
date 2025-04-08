from rest_framework import serializers
from .models import Blog, Comment

class commentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'
        # fields = ['id', 'blog', 'content', 'created_at', 'updated_at']

class blogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'
        # fields = ['id', 'title', 'content', 'created_at', 'updated_at']
 
 