# Generated by Django 4.1.7 on 2023-03-23 09:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chitchat', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'verbose_name': 'автор', 'verbose_name_plural': 'авторы'},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'категория', 'verbose_name_plural': 'категории'},
        ),
        migrations.AlterModelOptions(
            name='comment',
            options={'verbose_name': 'комментарий', 'verbose_name_plural': 'комментарии'},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'verbose_name': 'новость', 'verbose_name_plural': 'новости'},
        ),
        migrations.AlterField(
            model_name='author',
            name='authorUser',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='автор'),
        ),
        migrations.AlterField(
            model_name='author',
            name='ratingAuthor',
            field=models.IntegerField(default=0, verbose_name='рейтинг'),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(max_length=50, unique=True, verbose_name='название'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='comment',
            field=models.TextField(verbose_name='комментарий'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='post_comment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chitchat.post', verbose_name='статья'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='rating',
            field=models.IntegerField(default=0, verbose_name='рейтинг'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='user_comment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='автор'),
        ),
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chitchat.author', verbose_name='автор'),
        ),
        migrations.AlterField(
            model_name='post',
            name='post_type',
            field=models.CharField(choices=[('N', 'Новость'), ('A', 'Статья')], default='A', max_length=1, verbose_name='тип новости'),
        ),
        migrations.AlterField(
            model_name='post',
            name='rating',
            field=models.IntegerField(default=0, verbose_name='рейтинг'),
        ),
        migrations.AlterField(
            model_name='post',
            name='text',
            field=models.TextField(verbose_name='текст'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=100, unique=True, verbose_name='заголовок'),
        ),
    ]
