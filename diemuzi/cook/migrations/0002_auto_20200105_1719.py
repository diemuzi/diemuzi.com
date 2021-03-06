# Generated by Django 3.0.2 on 2020-01-05 23:19

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cook', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='cook',
            name='account',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='cook',
            name='category',
            field=models.ForeignKey(help_text='Select a category to associate this recipe to.', on_delete=django.db.models.deletion.CASCADE, to='cook.Category'),
        ),
        migrations.AddField(
            model_name='comment',
            name='account',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='+', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='comment',
            name='cook',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='cook.Cook'),
        ),
    ]
