# Generated by Django 4.2.4 on 2023-08-17 20:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('code_files', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='uploadedfile',
            name='is_checked',
            field=models.BooleanField(default=False),
        ),
    ]
