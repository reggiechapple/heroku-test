# Generated by Django 2.2.13 on 2020-08-17 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drinks', '0005_auto_20200817_0619'),
    ]

    operations = [
        migrations.AddField(
            model_name='drink',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='photos/glassware/%Y/%m/%d/'),
        ),
    ]
