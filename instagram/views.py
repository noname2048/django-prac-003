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


from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.permissions import IsAuthenticated
from . import permissions
from rest_framework.filters import SearchFilter, OrderingFilter


class PostViewSet(ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = PostSerializer
    # permission_classes = [IsAuthenticated]
    permission_classes = [permissions.IsAuthorOrReadOnly]

    filter_backends = [SearchFilter, OrderingFilter]
    search_fields = ["message"]  # ?search=
    ordering_fields = ["pk", "created_at"]  # ?ordering= 정렬을 허용할 필드의 화이트 스트
    ordering = ["pk"]  # 디폴트

    # def dispatch(self, request, *args, **kwargs):
    #     logger.info(
    #         f"request.body {request.body},\n" f"request.POST :{request.POST},\n"
    #     )
    #     return super().dispatch(request, *args, **kwargs)

    # authentication_classes = []

    def perform_create(self, serializer):
        ip = self.request.META["REMOTE_ADDR"]
        author = self.request.user  # User or Annoymous
        serializer.save(
            ip=ip,
            author=author,
        )

    @action(detail=False, methods=["GET"])
    def public(self, request):
        qs = self.get_queryset().filter(is_public=True)
        serializer = self.get_serializer(qs, many=True)
        return Response(serializer.data)

    @action(detail=True, methods=["PATCH"])
    def set_public(self, request, pk):
        instance = self.get_object()
        instance.is_public = True
        instance.save(update_fields=["is_public"])
        serializer = self.get_serializer(instance, many=False)
        return Response(serializer.data)


from rest_framework import renderers


class PostDetailAPIView(generics.RetrieveAPIView):
    queryset = Post.objects.all()
    renderer_classes = [renderers.TemplateHTMLRenderer]
    template_name = "instagram/post_detail.html"

    def get(self, request, *args, **kwargs):
        post = self.get_object()
        return Response(
            {
                "post": PostSerializer(post).data,
            }
        )
