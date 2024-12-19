from django_filters import rest_framework as filters
from .models import Job

class JobFilter(filters.FilterSet):
    location = filters.CharFilter(field_name="job_location", lookup_expr="icontains")

    class Meta:
        model = Job
        fields = ["location"]
