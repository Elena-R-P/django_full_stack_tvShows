# Generated by Django 2.2.4 on 2021-03-24 12:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('tv_show_app', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='show',
            old_name='desc',
            new_name='show_desc',
        ),
        migrations.RenameField(
            model_name='show',
            old_name='network',
            new_name='show_network',
        ),
        migrations.RenameField(
            model_name='show',
            old_name='release_date',
            new_name='show_release_date',
        ),
        migrations.RenameField(
            model_name='show',
            old_name='title',
            new_name='show_title',
        ),
    ]
