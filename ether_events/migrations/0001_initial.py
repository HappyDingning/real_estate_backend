# Generated by Django 4.0.4 on 2022-04-29 15:19

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Income',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('holder', models.CharField(max_length=42, validators=[django.core.validators.MinLengthValidator(42)], verbose_name='Holder')),
                ('token_id', models.CharField(max_length=42, validators=[django.core.validators.MinLengthValidator(42)], verbose_name='Token ID')),
                ('value', models.CharField(max_length=42, validators=[django.core.validators.MinLengthValidator(42)], verbose_name='Value')),
            ],
        ),
    ]
