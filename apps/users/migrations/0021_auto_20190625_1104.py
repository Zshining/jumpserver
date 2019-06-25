# Generated by Django 2.1.7 on 2019-06-25 03:04

import common.fields.model
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0020_auto_20190612_1825'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='_otp_secret_key',
            field=common.fields.model.EncryptCharField(blank=True, max_length=128, null=True),
        ),
        migrations.AlterField(
            model_name='user',
            name='_private_key',
            field=common.fields.model.EncryptTextField(blank=True, max_length=5000, verbose_name='Private key'),
        ),
        migrations.AlterField(
            model_name='user',
            name='_public_key',
            field=common.fields.model.EncryptTextField(blank=True, max_length=5000, verbose_name='Public key'),
        ),
    ]
