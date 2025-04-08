from rest_framework import generics
from blogs.models import Blog, Comment
from blogs.serializers import blogSerializer ,commentSerializer
 

# Create your views here.


class BlogList(generics.ListCreateAPIView):
    queryset = Blog.objects.all()
    serializer_class =  blogSerializer


class CommentList(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = commentSerializer
    # queryset = Comment.objects.all()


class BlogDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = blogSerializer
    lookup_field = 'pk'  # Use 'pk' as the lookup field instead of 'id'

class CommentDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = commentSerializer
    lookup_field = 'pk'  # Use 'pk' as the lookup field instead of 'id'
        