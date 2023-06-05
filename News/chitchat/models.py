from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum
from django.urls import reverse
from django.utils.translation import gettext as _
from django.utils.translation import gettext_lazy

from django.core.cache import cache  # кеширование


class Author(models.Model):
    authorUser = models.OneToOneField(
        User,
        on_delete=models.CASCADE,
        verbose_name=gettext_lazy('Author'),
    )
    ratingAuthor = models.IntegerField(
        default=0,
        verbose_name=gettext_lazy('Rating'),
    )

    def update_rating(self):
        postRate = self.post_set.aggregate(postRating=Sum('rating')) #  метод _set позволяет реверсивно обратиться
# через связанное поле author модели Post к ID полю модели Author
        p_r = 0
        p_r += postRate.get("postRating")

        commentRate = self.authorUser.comment_set.aggregate(commentRating=Sum("rating"))
        c_r = 0
        c_r += commentRate.get("commentRating")

        self.ratingAuthor = p_r * 3 + c_r
        self.save()

    def __str__(self):
        return f'{self.authorUser}'

    class Meta:  #  Возвращает название категории во множественном или единственном числе в админпанеле
        verbose_name = _('Author')
        verbose_name_plural = _('Authors')


class Category(models.Model):
    name = models.CharField(
        max_length=50,
        unique=True,
        verbose_name=gettext_lazy('Category'),
        help_text=gettext_lazy('Enter a category name'),
    )
    users = models.ManyToManyField(User, through='Subscription')

    def __str__(self):
        return f'{self.name.title()}'

    class Meta:
        verbose_name = _('Category')
        verbose_name_plural = _('Categories')


class Post(models.Model):
    news = 'N'
    article = 'A'

    POST_TYPES = [
        (news, gettext_lazy('News')),
        (article, gettext_lazy('Article'))
    ]

    author = models.ForeignKey(
        Author,
        on_delete=models.CASCADE,
        verbose_name=gettext_lazy('Author'),
    )
    #  verbose_name определяет имя поля, которое будет отображаться в админ панели внутри каждой модели
    post_type = models.CharField(
        max_length=1,
        choices=POST_TYPES,
        default=article,
        verbose_name=gettext_lazy('Post type'),
        help_text=gettext_lazy('Choose a post type'),
    )
    time_creation = models.DateTimeField(auto_now_add=True)
    post_category = models.ManyToManyField(Category, through='PostCategory', verbose_name=gettext_lazy('Category'))
    title = models.CharField(
        max_length=100,
        unique=True,
        verbose_name=gettext_lazy('Heading'),
    )
    text = models.TextField(verbose_name=gettext_lazy('Text'))
    rating = models.IntegerField(default=0, verbose_name=gettext_lazy('Rating'))

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
        verbose_name = _('Post')
        verbose_name_plural = _('Posts')


class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Comment(models.Model):
    post_comment = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        verbose_name=gettext_lazy('Post'),
    )
    user_comment = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name=gettext_lazy('Author'),
    )
    comment = models.TextField(verbose_name=gettext_lazy('Comment'))
    time_creation = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(
        default=0,
        verbose_name=gettext_lazy('Rating'),
    )

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()

    def __str__(self):
        return f'{self.comment[0:40]}'

    class Meta:
        verbose_name = _('Comment')
        verbose_name_plural = _('Comments')


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
        verbose_name = _('Subscription')
        verbose_name_plural = _('Subscriptions')
