from celery import shared_task
import time
from .models import Post, Subscription
import datetime
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.conf import settings


@shared_task
def hello():
    time.sleep(10)
    print("Hello, world!")


@shared_task
def new_post_notification():
    last_week = datetime.datetime.now() - datetime.timedelta(days=7)
    posts = Post.objects.filter(time_creation__gte=last_week)
    print(f'{posts = }')
    categories = set(posts.values_list('post_category__id', flat=True))
    print(f'{categories = }')
    subscribers = set(Subscription.objects.filter(category__in=categories).values_list('user__email', flat=True))
    # (Category.objects.filter(name__in=categories).values_list('subscribers__email', flat=True))
    print(f'{subscribers = }')
    html_content = render_to_string(
        'daily_post.html',
        {
            'link': settings.SITE_URL,
            'posts': posts,
        }
    )
    msg = EmailMultiAlternatives(
        subject='Статьи за неделю',
        body='',
        from_email=settings.DEFAULT_FROM_EMAIL,
        to=subscribers,
    )
    msg.attach_alternative(html_content, 'text/html')
    msg.send()

