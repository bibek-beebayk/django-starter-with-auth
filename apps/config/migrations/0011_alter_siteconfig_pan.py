# Generated by Django 5.1.4 on 2024-12-05 08:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("config", "0010_siteconfig_pan"),
    ]

    operations = [
        migrations.AlterField(
            model_name="siteconfig",
            name="pan",
            field=models.CharField(
                blank=True, max_length=255, null=True, verbose_name="PAN Number"
            ),
        ),
    ]
