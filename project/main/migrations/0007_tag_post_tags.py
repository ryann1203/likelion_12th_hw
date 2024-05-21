# Generated by Django 5.0.4 on 2024-05-21 12:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0006_comment'),
    ]

    operations = [
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
            ],
        ),
        migrations.AddField(
            model_name='post',
            name='tags',
            field=models.ManyToManyField(blank=True, related_name='posts', to='main.tag'),
        ),
    ]
