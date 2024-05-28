from common.models import BaseModel
from django.db import models
from django.conf import settings


class Category(BaseModel):
    title = models.CharField(max_length=256)

    def __str__(self) -> str:
        return self.title


class Tag(BaseModel):
    title = models.CharField(max_length=256)

    def __str__(self) -> str:
        return self.title


class Post(BaseModel):
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="authors",
    )
    title = models.CharField(max_length=256)

    category = models.ForeignKey(
        Category, on_delete=models.CASCADE, related_name="categories"
    )

    content = models.TextField()
    image = models.ImageField(upload_to="blogs/")

    tag = models.ManyToManyField(Tag)

    views = models.IntegerField(default=0)

    is_published = models.BooleanField(default=False)
    recommended = models.BooleanField(default=False)

    def __str__(self) -> str:
        return self.title


class Comment(BaseModel):
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name="comments")
    comment = models.TextField()
    parent = models.ForeignKey(
        "self", on_delete=models.CASCADE, related_name="child", null=True, blank=True
    )

    def __str__(self):
        return f"comment by {self.author}"
