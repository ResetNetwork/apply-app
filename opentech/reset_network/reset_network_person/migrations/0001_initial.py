# Generated by Django 2.2.9 on 2020-02-04 11:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('images', '0003_customimage_drupal_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='ResetNetworkPerson',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('role', models.CharField(max_length=255)),
                ('about', models.TextField()),
                ('linkedin', models.URLField()),
                ('twitter', models.URLField()),
                ('image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='images.CustomImage')),
            ],
            options={
                'verbose_name': 'Reset Network Person',
                'verbose_name_plural': 'Reset Network People',
            },
        ),
    ]
