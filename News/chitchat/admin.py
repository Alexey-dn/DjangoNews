from django.contrib import admin
from .models import Author, Post, Category, Comment

from modeltranslation.admin import TranslationAdmin


class PostAdmin(admin.ModelAdmin):
    # list_display = [field.name for field in Post._meta.get_fields()]
    # list_display — это список или кортеж со всеми полями, которые вы хотите видеть в таблице с товарами
    # генерируем список имён всех полей для более красивого отображения
    list_display = ('title', 'rating')  # если нужны не все поля, оставляем только необходимые
    # list_filter = ('price', 'quantity', 'name')  # добавляем примитивные фильтры в нашу админку
    search_fields = ('title', 'text')  # тут всё очень похоже на фильтры из запросов в базу


class PostAuthor(admin.ModelAdmin):
    list_display = ('authorUser', 'ratingAuthor')
    search_fields = ('authorUser', 'ratingAuthor')


class PostComment(admin.ModelAdmin):
    list_display = ('comment', 'user_comment', 'post_comment')
    search_fields = ('post_comment', 'user_comment')


class CategoryAdmin(TranslationAdmin):
    model = Category


class AuthorAdmin(TranslationAdmin):
    model = Author


class PostAdmin(TranslationAdmin):
    model = Post


class CommentAdmin(TranslationAdmin):
    model = Comment


admin.site.register(Author, PostAuthor)
admin.site.register(Post, PostAdmin)  # Не забываем зарегистрировать модели, иначе мы не увидим их в админке.
admin.site.register(Category)
admin.site.register(Comment, PostComment)

