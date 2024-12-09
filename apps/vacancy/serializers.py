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
            "category",
        ]


class JobDetailSerializer(serializers.ModelSerializer):
    company = CompanyNameSerializer(read_only=True)
    category = JobCategorySerializer(read_only=True)
    related_jobs = serializers.SerializerMethodField()

    def get_related_jobs(self, obj):
        related_jobs = Job.objects.filter(category=obj.category).exclude(id=obj.id)[:3]
        return JobListSerializer(
            related_jobs, many=True, context={"request": self.context["request"]}
        ).data

    class Meta:
        model = Job
        fields = "__all__"
