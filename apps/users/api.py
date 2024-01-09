from django.conf import settings
from rest_framework import status
from rest_framework.decorators import action
from rest_framework.mixins import CreateModelMixin
from rest_framework.parsers import JSONParser, MultiPartParser
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import GenericViewSet, ModelViewSet
from rest_framework_simplejwt.tokens import RefreshToken

from adapters import Email
from apps.users.models import OTP, User
from apps.users.serializers import (
    UserCreateSerializer,
    UserListSerializer,
    UserProfileSerializer,
    UserSerializer,
    UserUpdateSerializer,
)


def get_tokens(user):
    refresh = RefreshToken.for_user(user)
    return {"refresh": str(refresh), "access": str(refresh.access_token)}


def get_response(user_res, tokens):
    user_res["access"] = tokens["access"]
    user_res["refresh"] = tokens["refresh"]
    return user_res


class UserCreateViewSet(CreateModelMixin, GenericViewSet):
    queryset = User.objects.all()
    serializer_class = UserCreateSerializer
    permission_classes = [AllowAny]

    @action(detail=False, methods=["POST"], url_path="validate-otp")
    def validate_otp(self, request):
        user = User.objects.get(id=request.data["id"])
        otp = user.otps.first()
        if otp.is_used:
            return Response({"detail": "Otp already used."}, status=400)
        if otp.is_expired:
            return Response({"detail": "Otp expired."}, status=400)
        if not request.data["otp"] == otp.otp:
            return Response({"detail": "Invalid otp."}, status=400)
        if otp.otp_type == "Registration":
            user.otp_verified = True
            user.is_active = True
            user.login_count += 1
            tokens = get_tokens(user)
            res = get_response(user.get_login_response(), tokens)
        elif otp.otp_type == "Password Reset":
            res = {"otp_id": otp.id}
        user.save()
        otp.is_used = True
        otp.save()
        # TODO: send email/message to user
        return Response(res, status=200)

    @action(detail=False, methods=["POST"], url_path="login")
    def login(self, request):
        req_data = request.data
        try:
            user = User.objects.get(
                **{settings.USERNAME_FIELD: req_data[settings.USERNAME_FIELD]}
            )
        except User.DoesNotExist:
            return Response({"detail": "Incorrect username or password."})
        if not user.otp_verified:
            return Response({"detail": "User not verified."}, status=400)
        match = user.check_password(req_data["password"])
        if not match:
            return Response({"detail": "Incorrect username or password"})
        user.login_count += 1
        user.save()
        tokens = get_tokens(user)
        login_res = get_response(user.get_login_response(), tokens)
        return Response(
            login_res,
            status=200,
        )

    @action(detail=False, methods=["POST"], url_path="generate-otp")
    def generate_otp(self, request):
        req_data = request.data
        try:
            user = User.objects.get(username=req_data["username"])
        except User.DoesNotExist:
            return Response({"detail": "Username does not exist."}, status=400)
        otp = OTP.create(user.id, "Registration")
        mail = Email()
        mail_data = {
            "subject": "Registration OTP",
            "message": f"Your otp is {otp.otp}. Please use it to verify your registration.",
            "to": [user.email],
        }
        mail.send(mail_data)
        return Response({}, status=200)

    @action(detail=False, methods=["POST"], url_path="request-password-reset")
    def request_password_reset(self, request):
        # TODO: should use phone?
        email = request.data.get("email")
        try:
            user = User.objects.get(email=email)
        except User.DoesNotExist:
            return Response({"detail": "User does not exist"}, status=400)
        otp = OTP.create(user.id, "Password Reset")
        mail = Email()
        mail_data = {
            "subject": "Password Reset OTP",
            "message": f"Your otp is {otp.otp}. Please use it to verify your registration.",
            "to": [user.email],
        }
        mail.send(mail_data)
        return Response({"user_id": user.id}, status=200)

    @action(detail=True, methods=["POST"], url_path="reset-password")
    def reset_password(self, request, pk):
        user = self.get_object()
        otp_id = request.data.get("otp_id")
        otp = OTP.objects.get(id=otp_id)
        if not (otp.is_used and otp.otp_type == "Password Reset"):
            return Response({"detail": "OTP error."}, status=400)
        password = request.data.get("password")
        # TODO: Password Validation
        user.set_password(password)
        user.save()
        # TODO: send mail to the user
        mail_data = {
            "subject": "Password Reset OTP",
            "message": f"Your password was successfully reset.",
            "to": [user.email],
        }
        mail = Email()
        mail.send(mail_data)
        tokens = get_tokens(user)
        login_res = get_response(user.get_login_response(), tokens)
        return Response(login_res, status=200)


class UserViewSet(ModelViewSet):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    parser_classes = [JSONParser, MultiPartParser]

    def get_serializer_class(self):
        if self.action == "list":
            return UserListSerializer
        if self.action in ["detail", "me"]:
            return UserProfileSerializer
        if self.action == "partial_update":
            return UserUpdateSerializer
        return super().get_serializer_class()

    def partial_update(self, request, *args, **kwargs):
        if not self.get_object() == request.user:
            return Response(
                {"detail": "You are forbidden to perform this action."},
                status=status.HTTP_403_FORBIDDEN,
            )
        return super().partial_update(request, *args, **kwargs)

    @action(detail=False, methods=["GET"])
    def me(self, request, *args, **kwargs):
        user = request.user
        serializer = self.get_serializer(user)
        return Response(serializer.data)
