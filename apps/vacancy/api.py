from rest_framework.viewsets import ReadOnlyModelViewSet

from apps.vacancy.filters import JobFilter
from .serializers import JobListSerializer, JobDetailSerializer
from .models import Job
from rest_framework.permissions import AllowAny
from rest_framework.filters import SearchFilter
from django_filters.rest_framework import DjangoFilterBackend


class JobViewSet(ReadOnlyModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobListSerializer
    permission_classes = [AllowAny]
    filter_backends = [SearchFilter, DjangoFilterBackend]
    search_fields = ["title", "description"]
    filterset_class = JobFilter

    def get_serializer_class(self):
        if self.action == "retrieve":
            return JobDetailSerializer
        return super().get_serializer_class()
