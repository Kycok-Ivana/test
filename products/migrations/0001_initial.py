# Generated by Django 2.2.3 on 2019-07-30 10:27

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('description', models.TextField(max_length=150)),
                ('content', models.TextField()),
                ('image', models.ImageField(upload_to='product')),
                ('price', models.FloatField()),
                ('count', models.IntegerField()),
            ],
            options={
                'verbose_name': 'Товар',
                'verbose_name_plural': 'Товар',
                'ordering': ['id'],
            },
        ),
    ]
