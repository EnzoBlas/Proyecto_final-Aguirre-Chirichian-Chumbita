# Generated by Django 4.0.5 on 2022-06-26 04:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_blog', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='author',
            new_name='author_id',
        ),
        migrations.RenameField(
            model_name='ranking',
            old_name='author',
            new_name='author_id',
        ),
    ]