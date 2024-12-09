from rest_framework import serializers

from core.libs.images import ImageKeySerializer
from .models import Company, Job, JobCategory


class CompanyNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = ["id", "name"]


class CompanyListSerializer(serializers.ModelSerializer):
    logo = ImageKeySerializer("small")

    class Meta:
        model = Company
        fields = ["id", "name", "logo", "description", "jobs_count"]


class JobCategorySerializer(serializers.ModelSerializer):
    image = ImageKeySerializer("small")

    class Meta:
        model = JobCategory
        fields = ["id", "name", "image", "jobs_count"]


class JobListSerializer(serializers.ModelSerializer):
    image = ImageKeySerializer("small")
    company = CompanyNameSerializer(read_only=True)
    category = JobCategorySerializer(read_only=True)

    class Meta:
        model = Job
        fields = [
            "id",
            "title",
            "image",
            "job_type",
            "min_salary",
            "max_salary",
            "currency",
            "job_location",
            "created_at",
            "company",
            "category"
        ]
