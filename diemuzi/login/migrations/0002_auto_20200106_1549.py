# Generated by Django 3.0.2 on 2020-01-06 21:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('login', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='account',
            options={'permissions': [('change_manage', 'Can change manage'), ('change_password', 'Can change password'), ('change_permission', 'Can change permissions'), ('view_manage', 'Can view manage'), ('view_password', 'Can view password'), ('view_permission', 'Can view permissions')]},
        ),
    ]