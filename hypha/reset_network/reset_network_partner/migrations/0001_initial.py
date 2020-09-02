# Generated by Django 2.2.16 on 2020-09-01 16:29

from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0045_assign_unlock_grouppagepermission'),
        ('images', '0003_customimage_drupal_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='ResetNetworkPartnersPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('social_text', models.CharField(blank=True, max_length=255)),
                ('intro', wagtail.core.fields.RichTextField(blank=True)),
                ('social_image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='images.CustomImage')),
            ],
            options={
                'verbose_name': 'Reset Network Partner Page',
            },
            bases=('wagtailcore.page', models.Model),
        ),
        migrations.CreateModel(
            name='ResetNetworkPartnerPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('social_text', models.CharField(blank=True, max_length=255)),
                ('name', models.CharField(max_length=100)),
                ('status', models.CharField(choices=[('current_partner', 'Current Partner'), ('alumni_partner', 'Alumni Partner')], default='current_partner', max_length=20)),
                ('type', models.CharField(choices=[('profit', 'For Profit'), ('non_profit', 'Non Profit')], default='non_profit', max_length=20)),
                ('description', wagtail.core.fields.RichTextField(blank=True)),
                ('url', models.URLField(verbose_name='Web URL')),
                ('logo_url', models.URLField(blank=True)),
                ('social_image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='images.CustomImage')),
            ],
            options={
                'abstract': False,
            },
            bases=('wagtailcore.page', models.Model),
        ),
    ]
