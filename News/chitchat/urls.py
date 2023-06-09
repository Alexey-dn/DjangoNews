from django.urls import path
# Импортируем созданное нами представление
from .views import (
    PostList, PostDetail, PostCreate, PostUpdate, PostDelete, PostSearch,
    ArticleCreate, subscriptions
)
from .views import IndexView



urlpatterns = [
    # path — означает путь.
    # В данном случае путь ко всем товарам у нас останется пустым,
    # чуть позже станет ясно почему.
    # Т.к. наше объявленное представление является классом,
    # а Django ожидает функцию, нам надо представить этот класс в виде view.
    # Для этого вызываем метод as_view.
    path('', PostList.as_view(), name='post_list'),
    path('<int:pk>', PostDetail.as_view(), name='post_detail'),
    # Если дженерик в файле views.py представлен в виде класса, то в path
    # обработчик записывается в виде as_view(), а если представлен функцией,
    # то PostDetail.название функции, которую мы предварительно импортируем
    path('create/', PostCreate.as_view(), name='post_create'),
    path('article/create/', ArticleCreate.as_view(), name='article_create'),
    path('<int:pk>/update', PostUpdate.as_view(), name='post_update'),
    path('<int:pk>/delete/', PostDelete.as_view(), name='post_delete'),
    path('search/', PostSearch.as_view(), name='post_search'),
    path('subscriptions/', subscriptions, name='subscriptions'),
    path('index/', IndexView.as_view()),
]
