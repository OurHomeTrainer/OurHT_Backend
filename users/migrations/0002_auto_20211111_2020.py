# Generated by Django 3.2.8 on 2021-11-11 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='age',
            field=models.IntegerField(null=True),
        ),
        migrations.AddField(
            model_name='user',
            name='weight',
            field=models.FloatField(null=True),
        ),
    ]