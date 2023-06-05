from django_filters import FilterSet, ModelChoiceFilter, DateTimeFilter, CharFilter
from django.forms import DateTimeInput
from django.utils.translation import gettext_lazy as _
from .models import Post, Category


# Создаем свой набор фильтров для модели Post.
# FilterSet, который мы наследуем,
# должен чем-то напомнить знакомые вам Django дженерики.

class PostFilter(FilterSet):
    title = CharFilter(
        lookup_expr='icontains',
        field_name='title',
        label=_('Heading'),
    )

    category = ModelChoiceFilter(
        field_name='postcategory__category',
        queryset=Category.objects.all(),
        label=_('Category'),
        empty_label=_('Any'),
    )
    date = DateTimeFilter(
        field_name='time_creation',
        lookup_expr='gt',
        label=_('Date'),
        widget=DateTimeInput(
            attrs={'type': 'date'},
        ),
    )
