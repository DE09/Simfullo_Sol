# Generated by Django 4.1.1 on 2022-11-30 06:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('simfulloapp', '0005_rename_chargeaat_airother_airother_chargeaat_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='airother',
            old_name='airother_chargeaAt',
            new_name='airother_chargeAt',
        ),
    ]
