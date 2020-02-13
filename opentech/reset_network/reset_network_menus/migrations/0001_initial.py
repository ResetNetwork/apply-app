# Generated by Django 2.2.9 on 2020-02-04 11:42

from django.db import migrations, models
import django.db.models.deletion
import wagtail.core.blocks
import wagtail.core.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('wagtailcore', '0041_group_collection_permissions_verbose_name_plural'),
    ]

    operations = [
        migrations.CreateModel(
            name='ResetNetworkMenusMain',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('items', wagtail.core.fields.StreamField([('item', wagtail.core.blocks.StructBlock([('page', wagtail.core.blocks.PageChooserBlock()), ('title', wagtail.core.blocks.CharBlock(help_text="Leave blank to use the page's own title", required=False))]))], blank=True, verbose_name='Main menu')),
                ('site', models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, to='wagtailcore.Site')),
            ],
            options={
                'verbose_name': 'Reset Network Main Menu',
            },
        ),
        migrations.CreateModel(
            name='ResetNetworkMenusFooter',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('items', wagtail.core.fields.StreamField([('item', wagtail.core.blocks.StructBlock([('page', wagtail.core.blocks.PageChooserBlock()), ('title', wagtail.core.blocks.CharBlock(help_text="Leave blank to use the page's own title", required=False))]))], blank=True, verbose_name='Footer menu')),
                ('site', models.OneToOneField(editable=False, on_delete=django.db.models.deletion.CASCADE, to='wagtailcore.Site')),
            ],
            options={
                'verbose_name': 'Reset Network Footer Menu',
            },
        ),
    ]
