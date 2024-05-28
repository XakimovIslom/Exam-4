from rest_framework import generics
from rest_framework.permissions import IsAuthenticated, AllowAny
from blog.models import Post, Comment
from blog.serializers import (
    CommentSerializer,
    PostSerializer,
    PostCreateSerializer,
    
)
from django.utils.timezone import now, timedelta


class PostListAPIView(generics.ListAPIView):
    queryset = Post.objects.filter(is_published=True)
    serializer_class = PostSerializer


class PostNewestListAPIView(generics.ListAPIView):
    serializer_class = PostSerializer

    def get_queryset(self):
        queryset = Post.objects.filter(is_published=True).order_by("-id")
        return queryset


class MostViewedPostsAPIView(generics.ListAPIView):
    queryset = Post.objects.filter(is_published=True).order_by("-views")[:8]
    serializer_class = PostSerializer


class MostViewedOnOneWeekPostsAPIView(generics.ListAPIView):
    queryset = Post.objects.filter(is_published=True, created_at__gt=now() - timedelta(days=7))
    serializer_class = PostSerializer


class MostViewedOnOneMonthPostsAPIView(generics.ListAPIView):
    queryset = Post.objects.filter(is_published=True, created_at__gt=now() - timedelta(days=30))
    serializer_class = PostSerializer


class RecommendedPostsAPIView(generics.ListAPIView):
    queryset = Post.objects.filter(is_published=True, recommended=True)
    serializer_class = PostSerializer


class PostCreateAPIView(generics.CreateAPIView):
    queryset = Post.objects.filter()
    permission_classes = (IsAuthenticated,)
    serializer_class = PostCreateSerializer

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class PostDetailAPIView(generics.RetrieveAPIView):
    queryset = Post.objects.filter(is_published=True)
    serializer_class = PostSerializer

    def get_object(self):
        obj = super().get_object()
        obj.views += 1
        obj.save()
        return obj
    



class PostCommentListView(generics.ListAPIView):
    serializer_class = CommentSerializer
    permission_classes = (AllowAny,)

    def get_queryset(self):
        post_id = self.kwargs["pk"]
        queryset = Comment.objects.filter(post__id=post_id)
        return queryset


class PostCommentCreateView(generics.CreateAPIView):
    serializer_class = CommentSerializer
    permission_classes = (IsAuthenticated,)

    def perform_create(self, serializer):
        post_id = self.kwargs["pk"]
        serializer.save(author=self.request.user, post_id=post_id)
