# Generated by Django 5.2.3 on 2025-06-10 18:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes', '0002_notes_likes'),
    ]

    operations = [
        migrations.AlterField(
            model_name='notes',
            name='likes',
            field=models.PositiveSmallIntegerField(default=0),
        ),
    ]
