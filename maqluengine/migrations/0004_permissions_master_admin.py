# Generated by Django 2.0.2 on 2018-04-12 16:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maqluengine', '0003_auto_20180406_1747'),
    ]

    operations = [
        migrations.AddField(
            model_name='permissions',
            name='master_admin',
            field=models.BooleanField(default=False),
        ),
    ]
