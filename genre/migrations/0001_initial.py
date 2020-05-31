# Generated by Django 3.0.6 on 2020-05-25 14:36

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
            name='Genre',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255, unique=True)),
                ('slug', models.SlugField(allow_unicode=True, unique=True)),
                ('description', models.TextField(blank=True, default='')),
                ('description_html', models.TextField(blank=True, default='', editable=False)),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='GenreFellow',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('genre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='fellowships', to='genre.Genre')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='user_genre', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'unique_together': {('genre', 'user')},
            },
        ),
        migrations.AddField(
            model_name='genre',
            name='fellows',
            field=models.ManyToManyField(through='genre.GenreFellow', to=settings.AUTH_USER_MODEL),
        ),
    ]
