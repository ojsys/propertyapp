# Generated by Django 4.0.6 on 2022-09-17 10:38

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('rent', '0005_rent_file_delete_files'),
    ]

    operations = [
        migrations.RenameField(
            model_name='rent',
            old_name='file',
            new_name='files',
        ),
    ]
