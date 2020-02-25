# Generated by Django 2.0.13 on 2019-08-06 22:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application_projects', '0008_add_value_validator'),
    ]

    operations = [
        migrations.CreateModel(
            name='DocumentCategory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=254)),
                ('recommended_minimum', models.PositiveIntegerField()),
            ],
            options={
                'ordering': ('name',),
                'verbose_name_plural': 'Document Categories',
            },
        ),
    ]