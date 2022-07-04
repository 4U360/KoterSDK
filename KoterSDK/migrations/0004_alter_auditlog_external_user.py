# Generated by Django 4.0.5 on 2022-07-03 23:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('KoterSDK', '0003_auditlog_location'),
    ]

    operations = [
        migrations.AlterField(
            model_name='auditlog',
            name='external_user',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='KoterSDK.externaluser', verbose_name='External User'),
        ),
    ]