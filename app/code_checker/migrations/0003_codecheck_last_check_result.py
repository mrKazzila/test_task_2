# Generated by Django 4.2.4 on 2023-08-20 21:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('code_checker', '0002_alter_checklog_options_alter_codecheck_options_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='codecheck',
            name='last_check_result',
            field=models.TextField(default='', max_length=3000, verbose_name='Last check result'),
        ),
    ]
