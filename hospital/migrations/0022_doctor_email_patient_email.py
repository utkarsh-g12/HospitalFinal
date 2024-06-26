# Generated by Django 5.0.4 on 2024-05-16 21:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hospital', '0021_alter_order_status_alter_product_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='doctor',
            name='email',
            field=models.EmailField(blank=True, help_text='A valid email address, please.', max_length=100),
        ),
        migrations.AddField(
            model_name='patient',
            name='email',
            field=models.EmailField(blank=True, help_text='A valid email address, please.', max_length=100),
        ),
    ]
