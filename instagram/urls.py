from django.urls import path, include
from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register("posts", views.PostViewSet)

urlpatterns = [
    # path("public/", views.PostViewSet)
    # path("public/", views.PublicPostListAPIView.as_view()),
    path("public2/", views.PostListAPIView.as_view()),
    path("public3/", views.public_post_list),
    path("", include(router.urls)),
    path("mypost/<int:pk>/", views.PostDetailAPIView.as_view()),
]
