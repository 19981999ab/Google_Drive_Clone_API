# Generated by Django 2.2.1 on 2019-06-18 00:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_auto_20190618_0609'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='file',
            name='owner',
        ),
    ]
