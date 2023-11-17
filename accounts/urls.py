from django.urls import path
from . import views
app_name = 'auth'

urlpatterns = [
    path('signup/', views.register_view, name='signup'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('pf/',views.profile, name='profile')
]
