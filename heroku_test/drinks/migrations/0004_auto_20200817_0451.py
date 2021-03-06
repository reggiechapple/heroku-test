# Generated by Django 2.2.13 on 2020-08-17 04:51

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('drinks', '0003_auto_20200817_0439'),
    ]

    operations = [
        migrations.CreateModel(
            name='Technique',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(blank=True, max_length=128, unique=True)),
                ('name', models.CharField(blank=True, max_length=100, unique=True)),
            ],
            options={
                'verbose_name': 'technique',
                'verbose_name_plural': 'techniques',
            },
        ),
        migrations.AddField(
            model_name='drink',
            name='technique',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='drinks', to='drinks.Category'),
        ),
        migrations.AlterField(
            model_name='drink',
            name='category',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='drinks', to='drinks.Technique'),
        ),
    ]
