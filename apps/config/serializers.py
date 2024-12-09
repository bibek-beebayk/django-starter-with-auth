from rest_framework.serializers import ModelSerializer

from core.libs.images import ImageKeySerializer
from .models import Link, Testimonial, SiteConfig


class TestimonialSerializer(ModelSerializer):
    image = ImageKeySerializer("small")

    class Meta:
        model = Testimonial
        fields = "__all__"


class LinkSerializer(ModelSerializer):
    logo = ImageKeySerializer("small")

    class Meta:
        model = Link
        fields = ["title", "logo", "link"]


class SiteConfigSerializer(ModelSerializer):
    # logo = ImageKeySerializer("small")
    social_links = LinkSerializer(many=True, read_only=True)

    class Meta:
        model = SiteConfig
        fields = [
            "site_title",
            "social_links",
            "phone_numbers",
            "emails",
            "address",
            "google_maps_link",
        ]
