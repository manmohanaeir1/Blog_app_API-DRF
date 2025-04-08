from rest_framework import generics
from blogs.models import Blog
from blogs.serializers import blogSerializer ,commentSerializer
 

# Create your views here.


class BlogList(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class =  blogSerializer


class CommentList(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class = commentSerializer
    # queryset = Comment.objects.all()
    