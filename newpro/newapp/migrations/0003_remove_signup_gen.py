# Generated by Django 4.1.2 on 2022-12-03 04:05

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('newapp', '0002_rename_compname_signup_compname'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='signup',
            name='gen',
        ),
    ]