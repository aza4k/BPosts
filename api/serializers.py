from rest_framework.serializers import *
from post.models import Post

class PostSerializer(ModelSerializer):

    class Meta:

        model = Post
        fields = '__all__'