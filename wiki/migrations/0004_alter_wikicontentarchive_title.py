# Generated by Django 4.0.4 on 2023-04-30 09:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wiki', '0003_wikicontent_is_updating_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wikicontentarchive',
            name='title',
            field=models.CharField(max_length=255),
        ),
    ]
