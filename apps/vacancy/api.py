from rest_framework.viewsets import ReadOnlyModelViewSet
from .serializers import JobListSerializer, JobDetailSerializer
from .models import Job
from rest_framework.permissions import AllowAny


class JobViewSet(ReadOnlyModelViewSet):
    queryset = Job.objects.all()
    serializer_class = JobListSerializer
    permission_classes = [AllowAny]

    def get_serializer_class(self):
        if self.action == "retrieve":
            return JobDetailSerializer
        return super().get_serializer_class()
