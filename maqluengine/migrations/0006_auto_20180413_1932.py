# Generated by Django 2.0.2 on 2018-04-13 19:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('maqluengine', '0005_securiymessage_date_created'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='SecuriyMessage',
            new_name='SecurityMessage',
        ),
    ]