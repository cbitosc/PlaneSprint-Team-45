# Generated by Django 4.2.2 on 2023-06-27 06:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0003_explore'),
    ]

    operations = [
        migrations.AddField(
            model_name='place',
            name='about',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AddField(
            model_name='place',
            name='city',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='place',
            name='country',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AlterField(
            model_name='place',
            name='description',
            field=models.CharField(max_length=30),
        ),
    ]
