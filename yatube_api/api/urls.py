from rest_framework import routers
from django.urls import path, include
from rest_framework.authtoken import views
from .views import PostViewSet, CommentViewSet, GroupViewSet

router = routers.DefaultRouter()

router.register(r'posts', PostViewSet, basename='posts')
router.register(r'posts/(?P<post_id>\d+)/comments',
                CommentViewSet, basename='comments')
router.register(r'groups', GroupViewSet, basename='groups')

urlpatterns = [
    path('v1/api-token-auth/', views.obtain_auth_token),
    path('v1/', include(router.urls))
]
