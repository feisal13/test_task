# Generated by Django 3.0 on 2019-12-13 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_auto_20191212_1749'),
    ]

    operations = [
        migrations.AddField(
            model_name='news',
            name='is_public',
            field=models.BooleanField(default=False),
        ),
    ]
