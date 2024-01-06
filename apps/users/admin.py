from django.contrib import admin

from .models import OTP, User, UserDetail


class UserDetailInline(admin.StackedInline):
    model = UserDetail

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ["id", "username", "email"]
    inlines = [UserDetailInline]


@admin.register(OTP)
class OTPAdmin(admin.ModelAdmin):
    list_display = ["otp", "otp_type", "user"]
