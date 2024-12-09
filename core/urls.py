from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter, SimpleRouter
from rest_framework_simplejwt.views import TokenRefreshView

from apps.users import api as user_api
from apps.config import api as config_api

router = DefaultRouter() if settings.DEBUG else SimpleRouter()

router.register("auth", user_api.UserCreateViewSet, basename="auth")
router.register("user", user_api.UserViewSet, basename="user")


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/v1/", include(router.urls)),
    path("api/v1/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("ckeditor5/", include("django_ckeditor_5.urls")),

    path("api/v1/home/", config_api.HomePageView.as_view(), name="home"),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# if settings.DEBUG:
#     urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
