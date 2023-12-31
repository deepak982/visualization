# Generated by Django 4.2.7 on 2023-11-20 12:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='data',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('end_year', models.IntegerField(blank=True, null=True)),
                ('intensity', models.IntegerField()),
                ('sector', models.CharField(max_length=255)),
                ('topic', models.CharField(max_length=255)),
                ('insight', models.TextField()),
                ('url', models.URLField()),
                ('region', models.CharField(max_length=255)),
                ('start_year', models.IntegerField(blank=True, null=True)),
                ('impact', models.IntegerField(blank=True, null=True)),
                ('added', models.DateTimeField()),
                ('published', models.DateTimeField()),
                ('country', models.CharField(blank=True, max_length=255)),
                ('relevance', models.IntegerField()),
                ('pestle', models.CharField(max_length=255)),
                ('source', models.CharField(max_length=255)),
                ('title', models.TextField()),
                ('likelihood', models.IntegerField()),
            ],
        ),
    ]
