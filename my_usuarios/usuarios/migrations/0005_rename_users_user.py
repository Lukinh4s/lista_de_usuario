# Generated by Django 4.2 on 2023-05-24 23:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0004_users_created_at_users_is_active'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Users',
            new_name='User',
        ),
    ]
