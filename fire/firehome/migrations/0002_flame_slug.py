# Generated by Django 3.0.2 on 2020-02-02 00:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('firehome', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='flame',
            name='slug',
            field=models.SlugField(default='firepost'),
        ),
    ]
