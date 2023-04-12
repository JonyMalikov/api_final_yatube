from django.urls import path, include
from rest_framework.routers import SimpleRouter

from .views import PostViewSet, GroupViewSet, CommentViewSet, FollowViewSet

router = SimpleRouter()

router.register('posts', PostViewSet, basename='posts')
router.register('groups', GroupViewSet, basename='groups')
router.register(r'posts\/(?P<post_id>[^/.]+)\/comments',
                CommentViewSet, basename='comments')
router.register('follow', FollowViewSet, basename='follow')

router_v1 = [
    path('', include(router.urls)),
    path('', include('djoser.urls.jwt')),
]
urlpatterns = [
    path('v1/', include(router_v1)),
]
