# Generated by Django 4.1.9 on 2023-11-05 16:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('learning_logs', '0004_remove_topic_fake_fieldddd'),
    ]

    operations = [
        migrations.RenameField(
            model_name='topic',
            old_name='tags',
            new_name='tags_new',
        ),
    ]
