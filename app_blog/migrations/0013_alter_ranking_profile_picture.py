# Generated by Django 4.0.5 on 2022-06-26 21:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_blog', '0012_alter_ranking_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ranking',
            name='profile_picture',
            field=models.CharField(blank=True, max_length=300, null=True),
        ),
    ]