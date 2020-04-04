# Generated by Django 3.0.5 on 2020-04-03 07:10

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('corona', '0004_auto_20200402_0647'),
    ]

    operations = [
        migrations.CreateModel(
            name='rescue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('state', models.CharField(max_length=100)),
                ('district', models.CharField(max_length=100)),
                ('address', models.TextField(max_length=100, null=True)),
                ('pincode', models.IntegerField()),
                ('user_phone', phonenumber_field.modelfields.PhoneNumberField(default='+91', max_length=128, region=None, unique=True)),
            ],
        ),
    ]
