# Generated by Django 5.1.4 on 2024-12-05 08:46

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "config",
            "0006_remove_siteconfig_addresses_alter_siteconfig_options_and_more",
        ),
    ]

    operations = [
        migrations.CreateModel(
            name="Person",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("position", models.CharField(max_length=255)),
                ("name", models.CharField(max_length=255)),
                ("email", models.EmailField(blank=True, max_length=254, null=True)),
                ("mobile", models.CharField(blank=True, max_length=255, null=True)),
                (
                    "config",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="people",
                        to="config.siteconfig",
                    ),
                ),
            ],
            options={
                "verbose_name_plural": "People",
            },
        ),
    ]
