# Generated by Django 4.0.5 on 2022-07-03 23:38

import KoterSDK.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('KoterSDK', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='auditlog',
            name='ip_address',
            field=KoterSDK.fields.EncryptedIPAddressField(blank=True, null=True, verbose_name='IP Address'),
        ),
    ]
