# Generated by Django 2.2.9 on 2020-02-07 11:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('images', '0003_customimage_drupal_id'),
        ('wagtaildocs', '0010_document_file_hash'),
        ('wagtailcore', '0041_group_collection_permissions_verbose_name_plural'),
    ]

    operations = [
        migrations.CreateModel(
            name='ResetNetworkAboutPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('content_heading', models.CharField(max_length=255, verbose_name='Heading')),
                ('content_text', models.TextField(blank=True, verbose_name='Text')),
                ('section_1_heading', models.CharField(blank=True, max_length=255, verbose_name='Heading')),
                ('section_1_text', models.TextField(blank=True, verbose_name='Text')),
                ('section_2_heading', models.CharField(blank=True, max_length=255, verbose_name='Heading')),
                ('section_2_text', models.TextField(blank=True, verbose_name='Text')),
                ('section_3_heading', models.CharField(blank=True, max_length=255, verbose_name='Heading')),
                ('section_3_text', models.TextField(blank=True, verbose_name='Text')),
                ('section_4_heading', models.CharField(blank=True, max_length=255, verbose_name='Heading')),
                ('section_4_text', models.TextField(blank=True, verbose_name='Text')),
                ('section_5_heading', models.CharField(blank=True, max_length=255, verbose_name='Heading')),
                ('section_5_text', models.TextField(blank=True, verbose_name='Text')),
                ('section_5_link_text', models.CharField(blank=True, max_length=255, verbose_name='Link text')),
                ('section_6_heading', models.CharField(blank=True, max_length=255, verbose_name='Heading')),
                ('section_6_text', models.TextField(blank=True, verbose_name='Text')),
                ('content_heading_gif_desktop', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtaildocs.Document', verbose_name='Heading image desktop')),
                ('content_heading_gif_mobile', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='wagtaildocs.Document', verbose_name='Heading image mobile')),
                ('section_1_image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='images.CustomImage', verbose_name='Image')),
                ('section_2_image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='images.CustomImage', verbose_name='Image')),
                ('section_3_image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='images.CustomImage', verbose_name='Image')),
                ('section_4_image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='images.CustomImage', verbose_name='Image')),
                ('section_5_image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='images.CustomImage', verbose_name='Image')),
                ('section_5_link', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='+', to='wagtailcore.Page', verbose_name='Link')),
                ('section_6_image', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='+', to='images.CustomImage', verbose_name='Image')),
            ],
            options={
                'verbose_name': 'Reset Network About Page',
            },
            bases=('wagtailcore.page',),
        ),
    ]
