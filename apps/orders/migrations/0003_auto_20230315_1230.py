# Generated by Django 2.2.7 on 2023-03-15 12:30

import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('coupons', '0002_auto_20230312_1237'),
        ('orders', '0002_auto_20230307_1642'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='coupon',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='orders', to='coupons.Coupon'),
        ),
        migrations.AddField(
            model_name='order',
            name='discount',
            field=models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(0), django.core.validators.MaxValueValidator(100)]),
        ),
    ]
