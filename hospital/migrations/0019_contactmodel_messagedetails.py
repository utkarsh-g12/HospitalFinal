# Generated by Django 5.0.4 on 2024-05-01 12:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0018_auto_20201015_2036'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name1', models.CharField(max_length=30)),
                ('email1', models.CharField(max_length=30)),
                ('message1', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='MessageDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=30)),
                ('email', models.CharField(max_length=30)),
                ('message', models.CharField(max_length=100)),
            ],
        ),
    ]
