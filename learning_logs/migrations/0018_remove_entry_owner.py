# Generated by Django 4.1.9 on 2023-12-26 04:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('learning_logs', '0017_entry_owner'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='entry',
            name='owner',
        ),
    ]
