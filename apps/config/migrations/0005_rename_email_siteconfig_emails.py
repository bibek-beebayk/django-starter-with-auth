# Generated by Django 5.1.4 on 2024-12-05 08:22

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("config", "0004_address_remove_siteconfig_address_and_more"),
    ]

    operations = [
        migrations.RenameField(
            model_name="siteconfig",
            old_name="email",
            new_name="emails",
        ),
    ]
