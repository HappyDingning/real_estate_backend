from django.db import models
from django.core.validators import MinLengthValidator


class BucketInfo(models.Model):
    file_type = models.CharField(max_length=9, choices=[('image', 'image'), ('json', 'json'), ('image_tmp', 'image_tmp')], blank=False, null=False, verbose_name='File Type')
    end_point = models.CharField(max_length=128, blank=False, null=False, verbose_name='End Point')
    name = models.CharField(max_length=128, blank=False, null=False, verbose_name='Name')


class RealEstateBaseInfo(models.Model):
    creator = models.CharField(max_length=42, validators=[MinLengthValidator(42)], verbose_name='Creator Address')
    name = models.CharField(max_length=128, verbose_name='Name')
    description = models.TextField(blank=True, null=True, verbose_name='Description')
