from django.contrib import admin
from .models import Application, Job, Company


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ("name", "address", "country", "phone", "email", "website")
    search_fields = ("name", "address", "country", "phone", "email", "website")


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = (
        "title",
        "company",
        "job_location",
        "job_type",
        "expiry_date",
        "job_level",
    )
    search_fields = (
        "title",
        "company"
    )
    list_filter = [
        "company",
        "job_location",
        "job_type",
        "job_level",
    ]


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ("job", "cv")
    search_fields = ("job",)