# Generated by Django 2.2.9 on 2020-03-03 15:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('reset_network_contact_us', '0002_auto_20200303_1238'),
    ]

    operations = [
        migrations.AlterField(
            model_name='resetnetworkcontactuspage',
            name='content_email',
            field=models.EmailField(blank=True, max_length=254, null=True, verbose_name='Email'),
        ),
    ]
