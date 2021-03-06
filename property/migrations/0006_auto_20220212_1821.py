# Generated by Django 2.2.24 on 2022-02-12 15:21

from django.conf import settings
from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('property', '0005_complaints'),
    ]

    operations = [
        migrations.AddField(
            model_name='flat',
            name='liked_by',
            field=models.ManyToManyField(related_name='likers', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='flat',
            name='owner_pure_phone',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, db_index=True, max_length=128, null=True, region=None, verbose_name='Нормальзованный номер владельца'),
        ),
    ]
