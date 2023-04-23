from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum
from django.urls import reverse

from django.core.cache import cache  # кеширование


class Author(models.Model):
    authorUser = models.OneToOneField(User, on_delete=models.CASCADE, verbose_name='автор')
    ratingAuthor = models.IntegerField(default=0, verbose_name='рейтинг')

    def update_rating(self):
        postRate = self.post_set.aggregate(postRating=Sum('rating')) #  метод _set позволяет реверсивно обратиться
# через связанное поле author модели Post к ID полю модели Author
        p_r = 0
        p_r += postRate.get("postRating")

        commentRate = self.authorUser.comment_set.aggregate(commentRating=Sum("rating"))
        c_r = 0
        c_r += commentRate.get("commentRating")

       # c_p = 0
       #  for post in self.post_set.all():
       #      commentPostRate = post.comment_set.aggregate(commentPostRating=Sum('rating'))
       #      c_p += commentPostRate.get('commentPostRating')

        self.ratingAuthor = p_r * 3 + c_r
        self.save()

    def __str__(self):
        return f'{self.authorUser}'

    class Meta:  #  Возвращает название категории во множественном или единственном числе в админпанеле
        verbose_name = 'автор'
        verbose_name_plural = 'авторы'


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True, verbose_name='название')
    users = models.ManyToManyField(User, through='Subscription')

    def __str__(self):
        return f'{self.name.title()}'

    class Meta:
        verbose_name = 'категория'
        verbose_name_plural = 'категории'


class Post(models.Model):
    news = 'N'
    article = 'A'

    POST_TYPES = [
        (news, 'Новость'),
        (article, 'Статья')
    ]

    author = models.ForeignKey(Author, on_delete=models.CASCADE, verbose_name='автор')
    #  verbose_name определяет имя поля, которое будет отображаться в админ панели внутри каждой модели
    post_type = models.CharField(
        max_length=1, choices=POST_TYPES,
        default=article, verbose_name='тип новости'
    )
    time_creation = models.DateTimeField(auto_now_add=True)
    post_category = models.ManyToManyField(Category, through='PostCategory')
    title = models.CharField(max_length=100, unique=True, verbose_name='заголовок')
    text = models.TextField(verbose_name='текст')
    rating = models.IntegerField(default=0, verbose_name='рейтинг')

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()

    def preview(self):
        return f"{self.text[0:124]}..."

    def __str__(self):
        return f'{self.text.title()}'

    def get_absolute_url(self):
        return reverse('post_detail', args=[str(self.id)])

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)  # сначала вызываем метод родителя, чтобы объект сохранился
        cache.delete(f'post-{self.pk}')  # затем удаляем его из кэша, чтобы сбросить его

    class Meta:
        verbose_name = 'новость'
        verbose_name_plural = 'новости'


class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Comment(models.Model):
    post_comment = models.ForeignKey(Post, on_delete=models.CASCADE, verbose_name='статья')
    user_comment = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name='автор')
    comment = models.TextField(verbose_name='комментарий')
    time_creation = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0, verbose_name='рейтинг')

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()

    def __str__(self):
        return f'{self.comment[0:40]}'

    class Meta:
        verbose_name = 'комментарий'
        verbose_name_plural = 'комментарии'


class Subscription(models.Model):
    user = models.ForeignKey(
        to=User,
        on_delete=models.CASCADE,
        related_name='subscriptions',
    )
    category = models.ForeignKey(
        to='Category',
        on_delete=models.CASCADE,
        related_name='subscriptions',
    )

    class Meta:
        verbose_name = 'Подписка'
        verbose_name_plural = 'Подписки'
