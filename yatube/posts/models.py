from django.contrib.auth import get_user_model
from django.db import models

from core.models import CreatedModel

User = get_user_model()


class Group(models.Model):
    title = models.CharField("page title", max_length=200)
    slug = models.SlugField("group id", unique=True)
    description = models.TextField("group description")

    class Meta:
        verbose_name = "group"
        verbose_name_plural = "groups"

    def __str__(self) -> str:
        return self.title


class Post(CreatedModel):
    STRING_LENGTH = 15
    text = models.TextField("Текс поста", help_text="Введите текст поста")
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="posts",
        verbose_name="Автор поста",
    )
    image = models.ImageField(
        "Картинка",
        upload_to="posts/",
        blank=True,
    )
    group = models.ForeignKey(
        Group,
        blank=True,
        null=True,
        on_delete=models.SET_NULL,
        related_name="posts",
        verbose_name="Группа",
        help_text="Связанная группа",
    )

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"
        ordering = ["-pub_date"]

    def __str__(self) -> str:
        return self.text[: Post.STRING_LENGTH]


class Comment(CreatedModel):
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments"
    )
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name="Автор комментария",
    )
    text = models.TextField(
        "Текст комментария",
    )

    class Meta:
        verbose_name = "Комментарий"
        verbose_name_plural = "Комментарии"
        ordering = ["-pub_date"]

    def __str__(self) -> str:
        return self.text


class Follow(models.Model):
    author = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="following",
    )
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        related_name="follower",
    )
