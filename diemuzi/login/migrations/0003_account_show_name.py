# Generated by Django 3.0.2 on 2020-01-10 15:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0002_auto_20200106_1549'),
    ]

    operations = [
        migrations.AddField(
            model_name='account',
            name='show_name',
            field=models.BooleanField(default=True, help_text='Choose if your name should be shown after making a comment.', verbose_name='Show Name'),
        ),
    ]
