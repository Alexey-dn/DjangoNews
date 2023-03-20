from django.contrib import admin
from .models import Author, Post, Category, Comment


admin.site.register(Author)
admin.site.register(Post)  # Не забываем зарегистрировать модели, иначе мы не увидим их в админке.
admin.site.register(Category)
admin.site.register(Comment)

