# Generated by Django 5.1.4 on 2024-12-05 09:29

import django_ckeditor_5.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("config", "0014_siteconfig_paid_up_capital_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="siteconfig",
            name="mission",
            field=django_ckeditor_5.fields.CKEditor5Field(blank=True, null=True),
        ),
        migrations.AddField(
            model_name="siteconfig",
            name="vision",
            field=django_ckeditor_5.fields.CKEditor5Field(blank=True, null=True),
        ),
    ]
