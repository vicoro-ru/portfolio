# Generated by Django 4.0.4 on 2022-04-28 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('miniBlog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='miniblog',
            name='publisTime',
            field=models.DateField(auto_now=True),
        ),
    ]
