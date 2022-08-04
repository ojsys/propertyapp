# Generated by Django 4.0.6 on 2022-08-02 09:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rent', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PropertyInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('property_name', models.CharField(max_length=255)),
                ('property_type', models.CharField(max_length=255)),
                ('property_location', models.CharField(max_length=255)),
                ('property_description', models.CharField(max_length=255)),
                ('property_owner', models.CharField(choices=[('Owner 1', 'Owner 1'), ('Owner 2', 'Owner 2'), ('Owner 3', 'Owner 3'), ('Owner 4', 'Owner 4')], max_length=255, null=True)),
                ('property_images', models.ImageField(upload_to='images/')),
            ],
        ),
        migrations.DeleteModel(
            name='Property',
        ),
    ]
