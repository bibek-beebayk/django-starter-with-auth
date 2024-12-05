# Generated by Django 5.1.4 on 2024-12-05 08:51

import versatileimagefield.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("config", "0007_person"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="siteconfig",
            options={
                "verbose_name": "Company Details",
                "verbose_name_plural": "Company Details",
            },
        ),
        migrations.AddField(
            model_name="person",
            name="image",
            field=versatileimagefield.fields.VersatileImageField(
                blank=True, null=True, upload_to="images/people/"
            ),
        ),
    ]
