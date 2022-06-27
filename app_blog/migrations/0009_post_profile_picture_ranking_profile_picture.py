# Generated by Django 4.0.5 on 2022-06-26 20:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app_blog', '0008_avatar'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='profile_picture',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app_blog.avatar'),
        ),
        migrations.AddField(
            model_name='ranking',
            name='profile_picture',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='app_blog.avatar'),
        ),
    ]