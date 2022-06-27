# Generated by Django 4.0.5 on 2022-06-27 05:41

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('author', models.CharField(max_length=30)),
                ('text', models.TextField()),
                ('due_date', models.DateField(auto_now=True)),
                ('post_id', models.IntegerField(max_length=30)),
            ],
            options={
                'ordering': ['-due_date'],
            },
        ),
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('author', models.CharField(max_length=30)),
                ('content', models.TextField()),
                ('due_date', models.DateField(auto_now=True)),
                ('profile_picture', models.ImageField(blank=True, null=True, upload_to='avatars')),
            ],
        ),
        migrations.CreateModel(
            name='Ranking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name_course', models.CharField(max_length=30)),
                ('author', models.CharField(max_length=30)),
                ('opinion', models.TextField()),
                ('score', models.IntegerField()),
                ('due_date', models.DateField(auto_now=True)),
                ('profile_picture', models.CharField(blank=True, max_length=300, null=True)),
                ('post_image', models.CharField(blank=True, max_length=300, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Avatar',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='avatars')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
