# Generated by Django 5.1.4 on 2024-12-06 07:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("vacancy", "0005_application"),
    ]

    operations = [
        migrations.AddField(
            model_name="application",
            name="status",
            field=models.CharField(
                choices=[
                    ("Pending", "Pending"),
                    ("Accepted", "Accepted"),
                    ("Rejected", "Rejected"),
                ],
                default="Pending",
                max_length=32,
            ),
        ),
    ]