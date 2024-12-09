from rest_framework.serializers import ModelSerializer

from core.libs.images import ImageKeySerializer
from .models import Testimonial


class TestimonialSerializer(ModelSerializer):
    image = ImageKeySerializer("small")
    class Meta:
        model = Testimonial
        fields = "__all__"