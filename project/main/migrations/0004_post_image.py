# Generated by Django 5.0.4 on 2024-04-26 14:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_post_weather'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='post/'),
        ),
    ]
