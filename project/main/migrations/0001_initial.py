# Generated by Django 5.0.4 on 2024-04-26 00:00

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('writer', models.CharField(max_length=30)),
                ('body', models.TextField()),
                ('pub_date', models.DateTimeField()),
            ],
        ),
    ]