# Generated by Django 4.0.4 on 2023-05-02 03:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wiki', '0005_wikicontentarchive_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='wikicontentarchive',
            name='content_id',
            field=models.IntegerField(default=0),
        ),
    ]