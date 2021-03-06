# Generated by Django 4.0.4 on 2022-05-07 16:03

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BucketInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('file_type', models.CharField(choices=[('image', 'image'), ('json', 'json'), ('image_tmp', 'image_tmp')], max_length=9, verbose_name='File Type')),
                ('end_point', models.CharField(max_length=128, verbose_name='End Point')),
                ('name', models.CharField(max_length=128, verbose_name='Name')),
            ],
        ),
        migrations.CreateModel(
            name='RealEstateBaseInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('creator', models.CharField(max_length=42, validators=[django.core.validators.MinLengthValidator(42)], verbose_name='Creator Address')),
                ('name', models.CharField(max_length=128, verbose_name='Name')),
                ('description', models.TextField(blank=True, null=True, verbose_name='Description')),
            ],
        ),
    ]
