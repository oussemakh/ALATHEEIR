# Generated by Django 2.1 on 2018-08-15 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='articles_Analyse',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('body', models.TextField()),
                ('detail', models.CharField(max_length=400)),
                ('slug', models.SlugField()),
                ('date', models.DateTimeField(auto_now=True)),
                ('picture', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='articles_News',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('body', models.TextField()),
                ('detail', models.CharField(max_length=400)),
                ('slug', models.SlugField()),
                ('date', models.DateTimeField(auto_now=True)),
                ('picture', models.ImageField(upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='articles_Tutorial',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('body', models.TextField()),
                ('detail', models.CharField(max_length=400)),
                ('slug', models.SlugField()),
                ('date', models.DateTimeField(auto_now=True)),
                ('picture', models.ImageField(upload_to='')),
            ],
        ),
    ]