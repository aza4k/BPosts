from django.urls import path, include
from .views import *
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

app_name = 'posts'

urlpatterns = [
    path('',home, name='home'),
    path('posts/', posts, name='posts'),
    path('posts/<int:pk>/', detail, name='detail'),
    path('accounts/', include('accounts.urls')),
    path('create/', post_create, name='create'),
    path('post/<int:post_id>/update/', post_update, name='update'),
    path('post/<int:post_id>/delete/', post_delete, name='delete'),
]
