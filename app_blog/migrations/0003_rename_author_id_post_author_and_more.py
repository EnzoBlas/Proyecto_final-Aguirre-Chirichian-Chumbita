# Generated by Django 4.0.5 on 2022-06-26 04:42

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app_blog', '0002_rename_author_post_author_id_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='post',
            old_name='author_id',
            new_name='author',
        ),
        migrations.RenameField(
            model_name='ranking',
            old_name='author_id',
            new_name='author',
        ),
    ]
