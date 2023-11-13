from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.status import *
from post.models import Post
from .serializers import PostSerializer
from rest_framework.permissions import IsAuthenticated
from .permissions import PostPermission, PostDetailPermission
from django.http import Http404  # Import Http404 for exception handling

class PostListAPIView(APIView):
    permission_classes = [PostPermission]

    def get(self, request):
        # Retrieve all posts
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True, context={'request': request})
        return Response(serializer.data)

    def post(self, request):
        # Create a new post
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PostDetailAPIView(APIView):
    def get(self, request, pk):
        post = Post.objects.get(pk=pk)
        serializer = PostSerializer(post)
        return Response(serializer.data, status=HTTP_200_OK)

    def patch(self,request,pk):
        post = Post.objects.get(pk=pk)
        serializer = PostSerializer(post, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=HTTP_202_ACCEPTED)
        return Response(serializer.errors, status=HTTP_400_BAD_REQUEST)


    def delete(self, request, pk):
        # Delete a specific post
        post = self.get_object(pk)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
