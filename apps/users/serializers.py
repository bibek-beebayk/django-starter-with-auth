from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from urllib.parse import urlparse
from django.core.files.uploadedfile import SimpleUploadedFile
import urllib.request
from django.conf import settings

from adapters import Email
from core.libs.images import ImageKeySerializer
from core.libs.serializers import CustomModelSerializer

from .models import OTP, User


class UserCreateSerializer(CustomModelSerializer):
    # access_token = serializers.SerializerMethodField()
    # google_token = serializers.CharField(
    #     max_length=255, allow_blank=True, allow_null=True, write_only=True
    # )
    # dp_url = serializers.CharField(
    #     max_length=255, allow_blank=True, allow_null=True, write_only=True
    # )

    def validate_password(self, password):
        if len(password) < 8:
            raise ValidationError("Password must be at least 8 characters long.")
        return password

    # def get_access_token(self, obj):
    #     if self.context["request"].data.get("access"):
    #         return self.context["request"].data.get("access")
    #     return ""

    def create(self, validated_data):
        """TODO: Refactor for google signup. Extra fields on register
        dp_url, google_token"""
        request = self.context["request"]
        password = validated_data.pop("password")
        # dp_url = validated_data.pop("dp_url")
        google_token = request.data.get("google_token", None)
        user = self.Meta.model(**validated_data)
        user.set_password(password)
        if google_token:
            dp_url = request.data.get("dp_url")
            basename = urlparse(dp_url).path.split("/")[-1]
            tmpfile, _ = urllib.request.urlretrieve(dp_url)
            user.profile_picture = SimpleUploadedFile(basename, open(tmpfile, "rb").read())
        user.save()
        if settings.VALIDATE_OTP:
            # TODO: send otp via email/phone
            otp = OTP.create(user.id, "Registration")
            mail = Email()
            mail_data = {
                "subject": "Registration OTP",
                "message": f"Your otp is {otp.otp}. Please use it to verify your registration.",
                "to": [user.email],
            }
            mail.send(mail_data)
        return user

    class Meta:
        model = User
        fields = [
            "id",
            "email",
            # "full_name",
            "password",
            "username",
            "profile_picture",
        ]
        extra_kwargs = {
            "password": {"write_only": True},
            "username": {"required": False, "allow_blank": True, "allow_null": True},
            "id": {"read_only": True},
            "profile_picture": {"read_only": True},
            # "dp_url": {"read_only": True}
            # "google_token": {"read_only": True},
        }


class UserUpdateSerializer(CustomModelSerializer):
    bio = serializers.CharField(max_length=4096)
    class Meta:
        model = User
        fields = ["bio", "phone_number", "profile_picture"]

    def update(self, instance, validated_data):
        bio = validated_data.get("bio")
        instance.user_details.bio = bio
        instance.user_details.save()
        return super().update(instance, validated_data)


class UserSerializer(CustomModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class UserListSerializer(CustomModelSerializer):
    class Meta:
        model = User
        fields = ["id", "username"]


class UserProfileSerializer(CustomModelSerializer):
    profile_picture = ImageKeySerializer("small")
    bio = serializers.ReadOnlyField(source="user_details.bio")
    full_name = serializers.ReadOnlyField(source='user_details.full_name')

    class Meta:
        model = User
        fields = [
            "username",
            "full_name",
            "user_type",
            "is_premium_user",
            "bio",
            "followers_count",
            "followings_count",
            "profile_picture",
            "posts_count",
        ]


# class CategorySerializer(CustomModelSerializer):
#     image = ImageKeySerializer("medium")
#     class Meta:
#         model = Category
#         fields = ["id", "name", "image"]
