# Generated by Django 4.0.5 on 2022-06-26 21:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_blog', '0011_alter_ranking_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ranking',
            name='profile_picture',
            field=models.ImageField(blank=True, null=True, upload_to='avatars'),
        ),
    ]