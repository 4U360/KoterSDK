# Generated by Django 4.0.5 on 2022-07-04 15:28

from django.db import migrations, models
import django.utils.timezone
import mirage.fields
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('KoterSDK', '0005_contact_date_pcm_contact_fingerpint_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='date_pcm',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='pcm_by_phone',
        ),
        migrations.AddField(
            model_name='contact',
            name='date_mcp',
            field=models.DateTimeField(default=django.utils.timezone.now, verbose_name='Date MCP'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contact',
            name='mcp_by_phone',
            field=mirage.fields.EncryptedTextField(blank=True, null=True, verbose_name='Marketing Communications Permission'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='pep',
            field=models.CharField(max_length=560, verbose_name='Publicly Exposed (Brazil)'),
        ),
        migrations.AlterField(
            model_name='contact',
            name='uuid',
            field=models.UUIDField(db_index=True, default=uuid.uuid4, editable=False),
        ),
        migrations.AlterField(
            model_name='externaluser',
            name='fingerprint',
            field=mirage.fields.EncryptedTextField(blank=True, verbose_name='Fingerprint'),
        ),
    ]
