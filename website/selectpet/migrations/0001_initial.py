# Generated by Django 3.1.7 on 2021-03-04 15:37

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Pet',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('hair', models.CharField(max_length=10)),
                ('size', models.CharField(max_length=10)),
            ],
        ),
    ]
