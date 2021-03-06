# Generated by Django 4.0.5 on 2022-07-03 15:41

import KoterSDK.fields
from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields
import mirage.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AuditLog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('message', mirage.fields.EncryptedTextField(verbose_name='Message')),
            ],
            options={
                'get_latest_by': 'modified',
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('status', models.IntegerField(choices=[(0, 'Inactive'), (1, 'Active')], default=1, verbose_name='status')),
                ('activate_date', models.DateTimeField(blank=True, help_text='keep empty for an immediate activation', null=True)),
                ('deactivate_date', models.DateTimeField(blank=True, help_text='keep empty for indefinite activation', null=True)),
                ('first_name', mirage.fields.EncryptedCharField(blank=True, max_length=120, verbose_name='First Name')),
                ('last_name', mirage.fields.EncryptedCharField(blank=True, max_length=120, verbose_name='Last Name')),
                ('phone', KoterSDK.fields.EncryptedPhonenumberField(db_index=True, max_length=254, region=None, verbose_name='Phone')),
                ('has_optin', models.BooleanField(default=False, verbose_name='Has Optin')),
                ('optin_origin', mirage.fields.EncryptedURLField(verbose_name='Source URL')),
                ('optin_additional_info', mirage.fields.EncryptedTextField(blank=True, verbose_name='Additional information about optin')),
                ('has_optout', models.BooleanField(default=False, verbose_name='Has optout')),
                ('optout_origin', mirage.fields.EncryptedURLField(blank=True, verbose_name='Optout Source URL')),
                ('optout_additional_info', mirage.fields.EncryptedTextField(blank=True, verbose_name='Additional opt-out information')),
            ],
            options={
                'verbose_name': 'Contact',
                'verbose_name_plural': 'Contacts',
            },
        ),
        migrations.CreateModel(
            name='ExternalUser',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('status', models.IntegerField(choices=[(0, 'Inactive'), (1, 'Active')], default=1, verbose_name='status')),
                ('activate_date', models.DateTimeField(blank=True, help_text='keep empty for an immediate activation', null=True)),
                ('deactivate_date', models.DateTimeField(blank=True, help_text='keep empty for indefinite activation', null=True)),
                ('first_name', models.CharField(blank=True, max_length=120, verbose_name='First Name')),
                ('last_name', models.CharField(blank=True, max_length=120, verbose_name='Last Name')),
                ('email', mirage.fields.EncryptedEmailField(blank=True, max_length=254, verbose_name='Email')),
                ('cpf', KoterSDK.fields.EncryptedCPFFIeld(blank=True, db_index=True, max_length=254, verbose_name='CPF')),
            ],
            options={
                'verbose_name': 'External User',
                'verbose_name_plural': 'External Users',
            },
        ),
        migrations.CreateModel(
            name='Webhook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('service', models.CharField(db_index=True, max_length=120, verbose_name='Service')),
                ('payload', mirage.fields.EncryptedJSONField(default=None, null=True, verbose_name='Payload')),
            ],
        ),
        migrations.AddIndex(
            model_name='webhook',
            index=models.Index(fields=['created'], name='KoterSDK_we_created_4d5209_idx'),
        ),
        migrations.AddField(
            model_name='auditlog',
            name='external_user',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, to='KoterSDK.externaluser', verbose_name='External User'),
        ),
    ]
