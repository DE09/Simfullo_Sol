# Generated by Django 4.1.1 on 2022-11-28 06:51

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('simfulloapp', '0002_air'),
    ]

    operations = [
        migrations.RenameField(
            model_name='air',
            old_name='cur_100',
            new_name='cur',
        ),
        migrations.RenameField(
            model_name='air',
            old_name='cur_1000',
            new_name='fsc',
        ),
        migrations.RenameField(
            model_name='air',
            old_name='cur_300',
            new_name='skdl',
        ),
        migrations.RenameField(
            model_name='air',
            old_name='cur_45',
            new_name='via',
        ),
        migrations.RemoveField(
            model_name='air',
            name='cur_500',
        ),
        migrations.RemoveField(
            model_name='air',
            name='cur_min',
        ),
        migrations.RemoveField(
            model_name='air',
            name='cur_nor',
        ),
    ]