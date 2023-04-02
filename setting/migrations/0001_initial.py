# Generated by Django 4.0.4 on 2023-04-02 04:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Setting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('user_id', models.IntegerField()),
                ('firstname', models.CharField(max_length=255)),
                ('middlename', models.CharField(max_length=255)),
                ('lastname', models.CharField(max_length=255)),
                ('birthday', models.DateField(blank=True, null=True)),
                ('parent_id', models.IntegerField()),
            ],
        ),
    ]
