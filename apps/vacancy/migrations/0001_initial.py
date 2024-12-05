# Generated by Django 5.1.4 on 2024-12-05 10:36

import django.db.models.deletion
import django_ckeditor_5.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Company",
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
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("name", models.CharField(max_length=255)),
                ("address", models.CharField(max_length=255)),
                ("country", models.CharField(max_length=255)),
                ("phone", models.CharField(blank=True, max_length=255, null=True)),
                ("email", models.EmailField(blank=True, max_length=254, null=True)),
                ("website", models.URLField(blank=True, null=True)),
                ("description", models.TextField(blank=True, null=True)),
                (
                    "logo",
                    models.ImageField(
                        blank=True, null=True, upload_to="images/company_logos/"
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="Job",
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
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("title", models.CharField(max_length=255)),
                ("description", django_ckeditor_5.fields.CKEditor5Field()),
                ("job_location", models.CharField(max_length=255)),
                (
                    "min_salary",
                    models.DecimalField(
                        decimal_places=2, max_digits=10, verbose_name="Minimum Salary"
                    ),
                ),
                (
                    "max_salary",
                    models.DecimalField(
                        decimal_places=2, max_digits=10, verbose_name="Maximum Salary"
                    ),
                ),
                (
                    "job_type",
                    models.CharField(
                        choices=[
                            ("Full Time", "Full Time"),
                            ("Part Time", "Part Time"),
                            ("Contract", "Contract"),
                            ("Internship", "Internship"),
                            ("Temporary", "Temporary"),
                        ],
                        max_length=255,
                    ),
                ),
                (
                    "salary_distribution_period",
                    models.CharField(
                        choices=[
                            ("Weekly", "Weekly"),
                            ("Monthly", "Monthly"),
                            ("Half Yearly", "Half Yearly"),
                            ("Yearly", "Yearly"),
                        ],
                        max_length=255,
                    ),
                ),
                ("expiry_date", models.DateField()),
                (
                    "job_level",
                    models.CharField(
                        choices=[
                            ("Entry Level", "Entry Level"),
                            ("Mid Level", "Mid Level"),
                            ("Expert Level", "Expert Level"),
                        ],
                        max_length=255,
                    ),
                ),
                (
                    "required_experience",
                    models.CharField(
                        choices=[
                            ("No Experience", "No Experience"),
                            ("1 Year", "1 Year"),
                            ("2 Years", "2 Years"),
                            ("3 Years", "3 Years"),
                            ("4 Years", "4 Years"),
                            ("5 Years", "5 Years"),
                            ("6 Years", "6 Years"),
                            ("7 Years", "7 Years"),
                            ("8 Years", "8 Years"),
                            ("9 Years", "9 Years"),
                            ("10 Years", "10 Years"),
                            ("10+ Years", "10+ Years"),
                        ],
                        max_length=255,
                    ),
                ),
                (
                    "required_education",
                    models.CharField(
                        choices=[
                            ("High School", "High School"),
                            ("Diploma", "Diploma"),
                            ("Bachelor", "Bachelor"),
                            ("Master", "Master"),
                            ("PhD", "PhD"),
                        ],
                        max_length=255,
                    ),
                ),
                (
                    "company",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="vacancy.company",
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
    ]
