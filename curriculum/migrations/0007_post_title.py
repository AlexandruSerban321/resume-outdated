# Generated by Django 2.2.2 on 2019-08-06 07:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('curriculum', '0006_post'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='title',
            field=models.CharField(default=1, max_length=100),
            preserve_default=False,
        ),
    ]
