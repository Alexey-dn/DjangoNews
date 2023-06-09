# Generated by Django 4.1.7 on 2023-06-03 20:07

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('chitchat', '0005_category_name_en_us_category_name_ru_post_text_en_us_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='author',
            options={'verbose_name': 'Author', 'verbose_name_plural': 'Authors'},
        ),
        migrations.AlterModelOptions(
            name='category',
            options={'verbose_name': 'Category', 'verbose_name_plural': 'Categories'},
        ),
        migrations.AlterModelOptions(
            name='comment',
            options={'verbose_name': 'Comment', 'verbose_name_plural': 'Comments'},
        ),
        migrations.AlterModelOptions(
            name='post',
            options={'verbose_name': 'Post', 'verbose_name_plural': 'Posts'},
        ),
        migrations.AlterModelOptions(
            name='subscription',
            options={'verbose_name': 'Subscription', 'verbose_name_plural': 'Subscriptions'},
        ),
        migrations.AlterField(
            model_name='author',
            name='authorUser',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Author'),
        ),
        migrations.AlterField(
            model_name='author',
            name='ratingAuthor',
            field=models.IntegerField(default=0, verbose_name='Rating'),
        ),
        migrations.AlterField(
            model_name='category',
            name='name',
            field=models.CharField(help_text='Enter a category name', max_length=50, unique=True, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='category',
            name='name_en_us',
            field=models.CharField(help_text='Enter a category name', max_length=50, null=True, unique=True, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='category',
            name='name_ru',
            field=models.CharField(help_text='Enter a category name', max_length=50, null=True, unique=True, verbose_name='Name'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='comment',
            field=models.TextField(verbose_name='Comment'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='post_comment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chitchat.post', verbose_name='Post'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='rating',
            field=models.IntegerField(default=0, verbose_name='Rating'),
        ),
        migrations.AlterField(
            model_name='comment',
            name='user_comment',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Author'),
        ),
        migrations.AlterField(
            model_name='post',
            name='author',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='chitchat.author', verbose_name='Author'),
        ),
        migrations.AlterField(
            model_name='post',
            name='post_type',
            field=models.CharField(choices=[('N', 'News'), ('A', 'Article')], default='A', help_text='Choose a post type', max_length=1, verbose_name='Post type'),
        ),
        migrations.AlterField(
            model_name='post',
            name='rating',
            field=models.IntegerField(default=0, verbose_name='Rating'),
        ),
        migrations.AlterField(
            model_name='post',
            name='text',
            field=models.TextField(verbose_name='Text'),
        ),
        migrations.AlterField(
            model_name='post',
            name='text_en_us',
            field=models.TextField(null=True, verbose_name='Text'),
        ),
        migrations.AlterField(
            model_name='post',
            name='text_ru',
            field=models.TextField(null=True, verbose_name='Text'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title',
            field=models.CharField(max_length=100, unique=True, verbose_name='Heading'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title_en_us',
            field=models.CharField(max_length=100, null=True, unique=True, verbose_name='Heading'),
        ),
        migrations.AlterField(
            model_name='post',
            name='title_ru',
            field=models.CharField(max_length=100, null=True, unique=True, verbose_name='Heading'),
        ),
    ]
