from datetime import datetime

from django.views.generic import ListView, DetailView
from .models import Post

from django.http import HttpResponse


class PostList(ListView):
    # Указываем модель, объекты которой мы будем выводить
    model = Post
    ordering = '-time_creation'
    # Поле, которое будет использоваться для сортировки объектов
    # Если '-time_creation', то будет идти сортировка по дате создания(от последней к ранней)
    # Если 'title', то по названию новостей
    template_name = 'news.html'
    # Указываем имя шаблона, в котором будут все инструкции о том,
    # как именно пользователю должны быть показаны наши объекты
    context_object_name = 'news'
    # Это имя списка, в котором будут лежать все объекты.
    # Его надо указать, чтобы обратиться к списку объектов в html-шаблоне.
    paginate_by = 2

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     # К словарю добавим текущую дату в ключ 'time_now'.
    #     context['time_now'] = datetime.utcnow()
    #     return context

class PostDetail(DetailView):
    # Модель всё та же, но мы хотим получать информацию по отдельному товару
    model = Post
    # Используем другой шаблон
    template_name = 'post.html'
    # Название объекта, в котором будет выбранный пользователем продукт
    context_object_name = 'post'


def multiply(request):
    number = request.GET.get('number')
    multiplier = request.GET.get('multiplier')

    try:
        result = int(number) * int(multiplier)
        html = f"<html><body>{number}*{multiplier}={result}</body></html>"
    except (ValueError, TypeError):
        html = f"<html><body>Invalid input.</body></html>"

    return HttpResponse(html)
