# Generated by Django 5.0.6 on 2024-05-28 18:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='recommended',
            field=models.BooleanField(default=False),
        ),
    ]
