# Generated by Django 3.1.7 on 2021-04-16 13:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cardiacsupplied',
            old_name='request',
            new_name='docnumber',
        ),
    ]
