# Generated by Django 2.0.3 on 2018-04-29 00:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dojo_ninjas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='dojo',
            name='desc',
            field=models.TextField(default='Enter description'),
            preserve_default=False,
        ),
    ]
