from django.db import models
from django.core.validators import MinLengthValidator

# class Income(models.Model):
#     holder = models.CharField(max_length=42, validators=[MinLengthValidator(42)], verbose_name='Holder')
#     token_id = models.CharField(max_length=42, validators=[MinLengthValidator(42)], verbose_name='Token ID')
#     value = models.CharField(max_length=42, validators=[MinLengthValidator(42)], verbose_name='Value')
#     date = models.DateTimeField(auto_now_add=True, null=True, verbose_name='Date')

# class IncomeDaily(models.Model):
#     holder = models.CharField(max_length=42, validators=[MinLengthValidator(42)], verbose_name='Holder')
#     value = models.CharField(max_length=42, validators=[MinLengthValidator(42)], verbose_name='Value')
#     date = models.DateField(auto_now_add=True, verbose_name='Date')

# class IncomeWeekly(models.Model):
#     holder = models.CharField(max_length=42, validators=[MinLengthValidator(42)], verbose_name='Holder')
#     value = models.CharField(max_length=42, validators=[MinLengthValidator(42)], verbose_name='Value')
#     date = models.DateField(auto_now_add=True, verbose_name='Date')

# class IncomeMonthly(models.Model):
#     holder = models.CharField(max_length=42, validators=[MinLengthValidator(42)], verbose_name='Holder')
#     value = models.CharField(max_length=42, validators=[MinLengthValidator(42)], verbose_name='Value')
#     date = models.DateField(auto_now_add=True, verbose_name='Date')
