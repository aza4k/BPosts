from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from post.models import Post
from .serializers import PostSerializer
from rest_framework.permissions import IsAuthenticated
from .permissions import PostPermission, PostDetailPermission

class PostListAPIView(APIView):
    permission_classes = [PostPermission]

    def get(self, request):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True,context= 
        {'request': request})
        return Response(serializer.data)

    def post(self, request):
        serializer = PostSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class PostDetailAPIView(APIView):
    permission_classes = [PostDetailPermission]

    def get_object(self, pk):
        try:
            return Post.objects.get(pk=pk)
        except Post.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        post = self.get_object(pk)
        serializer = PostSerializer(post,context= 
        {'request': request})
        return Response(serializer.data)

    def post(self, request, pk):
        # Logic for handling POST request on a specific post
        return Response("POST method not allowed on a specific post", status=status.HTTP_405_METHOD_NOT_ALLOWED)

    def put(self, request, pk):
        post = self.get_object(pk)
        serializer = PostSerializer(post, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk):
        post = self.get_object(pk)
        post.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
