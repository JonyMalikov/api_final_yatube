from django.urls import path, include
from rest_framework.routers import SimpleRouter

from .views import PostViewSet, GroupViewSet, CommentViewSet, FollowViewSet

router_v1 = SimpleRouter()

router_v1.register('posts', PostViewSet, basename='posts')
router_v1.register('groups', GroupViewSet, basename='groups')
router_v1.register(r'posts\/(?P<post_id>[^/.]+)\/comments',
                   CommentViewSet, basename='comments')
router_v1.register('follow', FollowViewSet, basename='follow')

router_v1 = [
    path('', include(router_v1.urls)),
    path('', include('djoser.urls.jwt')),
]
urlpatterns = [
    path('v1/', include(router_v1)),
]
