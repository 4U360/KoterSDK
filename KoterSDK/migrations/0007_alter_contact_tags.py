# Generated by Django 4.0.5 on 2022-07-06 12:54

from django.db import migrations
import tagulous.models.fields


class Migration(migrations.Migration):

    dependencies = [
        ('KoterSDK', '0006_remove_contact_date_pcm_remove_contact_pcm_by_phone_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='tags',
            field=tagulous.models.fields.TagField(_set_tag_meta=True, blank=True, help_text='Enter a comma-separated tag string', to='KoterSDK.tagulous_contact_tags', verbose_name='Tags'),
        ),
    ]
