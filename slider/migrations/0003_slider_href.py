# Generated by Django 2.2.3 on 2019-07-29 12:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('slider', '0002_auto_20190729_1251'),
    ]

    operations = [
        migrations.AddField(
            model_name='slider',
            name='href',
            field=models.CharField(max_length=100, null=True),
        ),
    ]