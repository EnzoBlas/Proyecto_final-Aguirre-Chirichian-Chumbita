# Generated by Django 4.0.5 on 2022-06-26 06:14

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_blog', '0004_alter_post_author'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ranking',
            name='author',
        ),
    ]
