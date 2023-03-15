from django.db import models
from django.contrib.auth.models import User
from django.db.models import Sum


class Author(models.Model):
    authorUser = models.OneToOneField(User, on_delete=models.CASCADE)
    ratingAuthor = models.IntegerField(default=0)

    def update_rating(self):
        postRate = self.post_set.aggregate(postRating=Sum('rating'))
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


class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)


class Post(models.Model):
    news = 'N'
    article = 'A'

    POST_TYPES = [
        (news, 'Новость'),
        (article, 'Статья')
    ]

    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    post_type = models.CharField(max_length=1, choices=POST_TYPES, default=article)
    time_creation = models.DateTimeField(auto_now_add=True)
    post_category = models.ManyToManyField(Category, through='PostCategory')
    title = models.CharField(max_length=100)
    text = models.TextField()
    rating = models.IntegerField(default=0)

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()

    def preview(self):
        return f"{self.text[0:124]}..."


class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Comment(models.Model):
    post_comment = models.ForeignKey(Post, on_delete=models.CASCADE)
    user_comment = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.TextField()
    time_creation = models.DateTimeField(auto_now_add=True)
    rating = models.IntegerField(default=0)

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()
