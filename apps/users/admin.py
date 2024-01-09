from django.contrib import admin

from .models import OTP, User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ["id", "username", "email"]


@admin.register(OTP)
class OTPAdmin(admin.ModelAdmin):
    list_display = ["otp", "otp_type", "user"]
