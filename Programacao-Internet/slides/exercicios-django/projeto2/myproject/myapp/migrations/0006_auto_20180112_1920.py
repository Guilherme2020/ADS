# Generated by Django 2.0 on 2018-01-12 19:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0005_auto_20180112_1913'),
    ]

    operations = [
        migrations.RenameField(
            model_name='membership',
            old_name='person',
            new_name='member',
        ),
    ]
