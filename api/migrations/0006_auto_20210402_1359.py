# Generated by Django 3.1.7 on 2021-04-02 08:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0005_auto_20210402_1304'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cardiacrequested',
            name='A_2A_qty',
            field=models.CharField(blank=True, default='0', max_length=100),
        ),
    ]