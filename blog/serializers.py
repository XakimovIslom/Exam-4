from rest_framework import serializers
from blog.models import Comment
from users.models import Account
from blog.models import Post


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = (
            "title",
            "category",
            "content",
            "image",
            "tag",
            "views",
            "created_at",
        )


class PostCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = (
            "title",
            "category",
            "content",
            "image",
            "tag",
        )

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Account
        fields = ("username",)


class CommentSerializer(serializers.ModelSerializer):
    author = AuthorSerializer(read_only=True)

    class Meta:
        model = Comment
        fields = [
            "id",
            "author",
            "post",
            "comment",
            "parent",
            "created_at",
        ]
