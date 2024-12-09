from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import AllowAny

from apps.config.models import SiteConfig, Testimonial
from apps.config.serializers import SiteConfigSerializer, TestimonialSerializer
from apps.vacancy.models import Application, Company, Job, JobCategory
from apps.vacancy.serializers import (
    CompanyListSerializer,
    JobCategorySerializer,
    JobListSerializer,
)


class ConfigView(APIView):
    
    permission_classes = [AllowAny]

    def get(self, request, *args, **kwargs):
        serializer = SiteConfigSerializer(
            SiteConfig.objects.first(), context={"request": request}
        )
        return Response(serializer.data)


class HomePageView(APIView):

    permission_classes = [AllowAny]

    def get(self, request):
        res = {}

        res["jobs_count"] = Job.objects.count()
        res["applications_count"] = Application.objects.count()  # TODO: fix
        res["companies_count"] = Company.objects.count()

        recent_jobs = Job.objects.all().order_by("-created_at")[:5]
        res["recent_jobs"] = JobListSerializer(
            recent_jobs, many=True, context={"request": request}
        ).data

        categories = JobCategory.objects.all().order_by("-name")
        res["categories"] = JobCategorySerializer(
            categories, many=True, context={"request": request}
        ).data

        top_companies = Company.objects.all().order_by("-created_at")[:4]
        res["top_companies"] = CompanyListSerializer(
            top_companies, many=True, context={"request": request}
        ).data

        testimonials = Testimonial.objects.order_by("-created_at")[:3]
        res["testimonials"] = TestimonialSerializer(
            testimonials, many=True, context={"request": request}
        ).data

        return Response(res)
