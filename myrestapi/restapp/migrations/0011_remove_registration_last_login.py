# Generated by Django 3.0.7 on 2020-06-25 13:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('restapp', '0010_auto_20200625_1832'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='registration',
            name='last_login',
        ),
    ]
