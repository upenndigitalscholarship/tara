# Generated by Django 2.0.2 on 2018-06-15 12:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('maqluengine', '0009_auto_20180606_1042'),
    ]

    operations = [
        migrations.AddField(
            model_name='formtype',
            name='primary_thumbnail_reference_pk',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
