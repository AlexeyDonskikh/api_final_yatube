from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import (TokenObtainPairView,
                                            TokenRefreshView)

from api.views import (CommentViewSet, FollowListView, GroupListView,
                       PostViewSet)

router = DefaultRouter()
router.register('posts', PostViewSet, basename="posts")
router.register(r'posts/(?P<post_id>\d+)/comments', CommentViewSet,
                basename="comments")


urlpatterns = [
    path('v1/', include(router.urls)),
    path('v1/token/', TokenObtainPairView.as_view(),
         name='token_obtain_pair'),
    path('v1/token/refresh/', TokenRefreshView.as_view(),
         name='token_refresh'),
    path('v1/follow/', FollowListView.as_view()),
    path('v1/group/', GroupListView.as_view()),
]
