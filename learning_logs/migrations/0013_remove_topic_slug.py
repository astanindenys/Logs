# Generated by Django 4.1.9 on 2023-12-26 04:15

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('learning_logs', '0012_topic_slug'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='topic',
            name='slug',
        ),
    ]