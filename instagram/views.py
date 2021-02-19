from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import PostSerializer
from .models import Post
from rest_framework import generics
import logging

logger = logging.getLogger("django.server")


class PublicPostListAPIView(generics.ListCreateAPIView):
    queryset = Post.objects.all()  # .filter(is_public=True)
    serializer_class = PostSerializer


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer

    # def dispatch(self, request, *args, **kwargs):
    #     logger.info(
    #         f"request.body {request.body},\n" f"request.POST :{request.POST},\n"
    #     )
    #     return super().dispatch(request, *args, **kwargs)


def post_list(request):
    pass


def post_detail(request, pk):
    pass
