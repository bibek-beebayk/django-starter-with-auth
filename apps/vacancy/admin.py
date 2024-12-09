from django.contrib import admin

from core.libs.admin import ReadOnlyModelAdmin
from .models import Application, Job, Company, JobCategory


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ["name", "address", "country", "phone", "email", "website"]
    search_fields = ["name", "address"]


@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = [
        "title",
        "company",
        "job_location",
        "job_type",
        "expiry_date",
        "job_level",
    ]
    search_fields = ["title", "company"]
    list_filter = [
        "company",
        "job_location",
        "job_type",
        "job_level",
    ]


@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ["job", "cv", "status"]
    search_fields = ["job"]
    list_filter = ["job", "status"]
    readonly_fields = ["job", "cv"]

    def has_add_permission(self, request):
        return False


@admin.register(JobCategory)
class JobCategoryAdmin(admin.ModelAdmin):
    list_display = ["name", "jobs_count"]
    search_fields = ["name"]
    readonly_fields = ["jobs_count"]
