# Generated by Django 3.0.5 on 2020-04-02 06:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('corona', '0002_auto_20200402_0619'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='hospitals',
            name='hContact',
        ),
    ]
