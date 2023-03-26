from django_filters import FilterSet, ModelChoiceFilter
from .models import Post, Category


# Создаем свой набор фильтров для модели Post.
# FilterSet, который мы наследуем,
# должен чем-то напомнить знакомые вам Django дженерики.

class PostFilter(FilterSet):

    category = ModelChoiceFilter(
        field_name='postcategory__category',
        queryset=Category.objects.all(),
        label='Категория',
        empty_label='Любая',
    )

    class Meta:
        # В Meta классе мы должны указать Django модель,
        # в которой будем фильтровать записи.
        model = Post
        # В fields мы описываем по каким полям модели
        # будет производиться фильтрация.
        fields = {
            # поиск по названию
            'title': ['icontains'],
            # 'postcategory__category': ['exact'],
            # количество товаров должно быть больше или равно
            # 'quantity': ['gt'],
            # 'price': [
            #     'lt',  # цена должна быть меньше или равна указанной
            #     'gt',  # цена должна быть больше или равна указанной
            # ],
        }
