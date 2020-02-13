# Generated by Django 2.2.9 on 2020-02-04 11:42

from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0041_group_collection_permissions_verbose_name_plural'),
    ]

    operations = [
        migrations.CreateModel(
            name='ResetNetworkBasicPage',
            fields=[
                ('page_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to='wagtailcore.Page')),
                ('content_text', wagtail.core.fields.RichTextField(verbose_name='Text')),
            ],
            options={
                'verbose_name': 'Reset Network Basic Page',
            },
            bases=('wagtailcore.page',),
        ),
    ]
