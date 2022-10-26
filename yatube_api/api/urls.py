from rest_framework import routers
from django.urls import path, include
from rest_framework.authtoken import views
from .views import PostViewSet, CommentViewSet, GroupViewSet

v1_router = routers.DefaultRouter()

v1_router.register('posts', PostViewSet, basename='posts')
v1_router.register(r'posts/(?P<post_id>\d+)/comments',
                   CommentViewSet, basename='comments')
v1_router.register('groups', GroupViewSet, basename='groups')

urlpatterns = [
    path('v1/api-token-auth/', views.obtain_auth_token),
    path('v1/', include(v1_router.urls))
]
