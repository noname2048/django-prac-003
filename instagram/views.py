from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import PostSerializer
from .models import Post
from rest_framework import generics
import logging
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.decorators import api_view

logger = logging.getLogger("django.server")


class PublicPostListAPIView(generics.ListAPIView):
    queryset = Post.objects.filter(is_public=True)
    serializer_class = PostSerializer


class PostListAPIView(APIView):
    def get(self, request, format=None):
        qs = Post.objects.filter(is_public=True)
        serializer = PostSerializer(qs, many=True)
        return Response(serializer.data)


@api_view(["GET"])
def public_post_list(request):
    qs = Post.objects.filter(is_public=True)
    serializer = PostSerializer(qs, many=True)
    return Response(serializer.data)


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
