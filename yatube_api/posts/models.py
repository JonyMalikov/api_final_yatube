from django.contrib.auth import get_user_model
from django.db import models

User = get_user_model()


class Group(models.Model):
    title = models.CharField(max_length=250, verbose_name='Заголовок')
    slug = models.SlugField(unique=True, verbose_name='URL')
    description = models.TextField(verbose_name='Описание группы')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Группа'
        verbose_name_plural = 'Группы'
        ordering = ['title']


class Post(models.Model):
    text = models.TextField(verbose_name='Статья')
    pub_date = models.DateTimeField(
        auto_now_add=True, verbose_name='Время создания')
    time_update = models.DateTimeField(
        auto_now=True, verbose_name="Время изменения")
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='posts',
        verbose_name='Автор статьи')
    group = models.ForeignKey(
        Group, blank=True, null=True, on_delete=models.SET_NULL,
        related_name='posts', verbose_name='Группа')
    image = models.ImageField(
        upload_to='posts/', blank=True, null=True,
        verbose_name='Изображение')

    class Meta:
        verbose_name = 'Статья'
        verbose_name_plural = 'Статьи'
        ordering = ['pub_date', 'author']

    def __str__(self):
        return self.text


class Comment(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, verbose_name='Автор коментария',
        related_name='comments')
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, verbose_name='Коментарий статьи',
        related_name='comments')
    text = models.TextField(verbose_name='Статья')
    created = models.DateTimeField(
        auto_now_add=True, db_index=True, verbose_name='Время создания')
    update = models.DateTimeField(
        auto_now=True, verbose_name="Время изменения")

    class Meta:
        verbose_name = 'Комментарий'
        verbose_name_plural = 'Комментарии'
        ordering = ['created', 'author']


class Follow(models.Model):
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='follower',
        verbose_name='Пользователь')
    following = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='following',
        verbose_name='Подписки пользователя')

    def __str__(self):
        return self.following
