from django.urls import path, include
from .views import PostListAPIView, PostDetailAPIView
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('posts/', PostListAPIView.as_view(), name='post-list'),
    path('posts/<int:pk>/', PostDetailAPIView.as_view(), name='post-detail'),
    path('auth/', include('dj_rest_auth.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
