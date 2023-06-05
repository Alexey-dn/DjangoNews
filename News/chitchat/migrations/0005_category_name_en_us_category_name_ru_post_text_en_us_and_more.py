# Generated by Django 4.1.7 on 2023-05-29 12:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chitchat', '0004_category_users'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='name_en_us',
            field=models.CharField(max_length=50, null=True, unique=True, verbose_name='название'),
        ),
        migrations.AddField(
            model_name='category',
            name='name_ru',
            field=models.CharField(max_length=50, null=True, unique=True, verbose_name='название'),
        ),
        migrations.AddField(
            model_name='post',
            name='text_en_us',
            field=models.TextField(null=True, verbose_name='текст'),
        ),
        migrations.AddField(
            model_name='post',
            name='text_ru',
            field=models.TextField(null=True, verbose_name='текст'),
        ),
        migrations.AddField(
            model_name='post',
            name='title_en_us',
            field=models.CharField(max_length=100, null=True, unique=True, verbose_name='заголовок'),
        ),
        migrations.AddField(
            model_name='post',
            name='title_ru',
            field=models.CharField(max_length=100, null=True, unique=True, verbose_name='заголовок'),
        ),
    ]
