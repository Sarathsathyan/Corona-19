# Generated by Django 3.0.5 on 2020-04-02 06:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('corona', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='hospitals',
            name='hContact',
            field=models.IntegerField(null=True),
        ),
    ]
