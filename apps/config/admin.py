from django.contrib import admin

from core.libs.admin import ReadOnlyModelAdmin
from .models import Link, SiteConfig, Person, Client, ContactUs, FAQ, Document, Page, Testimonial
from solo.admin import SingletonModelAdmin

admin.site.site_header = "Al Noor Admin"
admin.site.site_title = "Al Noor Admin Portal"


@admin.register(SiteConfig)
class SiteConfigAdmin(SingletonModelAdmin):
    fieldsets = [
        (
            "General",
            {
                "fields": [
                    "site_title",
                    "logo",
                    "government_license_number",
                    "company_registrar_number",
                    "pan",
                    "paid_up_capital",
                    "working_countries",
                ]
            },
        ),
        (
            "Contact Info",
            {
                "fields": [
                    "address",
                    "phone_numbers",
                    "emails",
                    "website",
                    "social_links",
                ]
            },
        ),
        (
            "Mission and Vision",
            {
                "fields": [
                    "mission",
                    "vision",
                ]
            },
        ),
    ]


@admin.register(Link)
class LinkAdmin(admin.ModelAdmin):
    list_display = ("title", "link")


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    list_display = ("position", "name", "email", "mobile")
    list_filter = ("position",)
    search_fields = ("position", "name", "email", "mobile")


@admin.register(Client)
class ClientAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)


@admin.register(ContactUs)
class ContactUsAdmin(ReadOnlyModelAdmin):
    list_display = ("first_name", "last_name", "email", "phone", "created_at")
    search_fields = ("first_name", "last_name", "email", "phone")


@admin.register(FAQ)
class FAQAdmin(admin.ModelAdmin):
    list_display = ("question",)
    search_fields = ("question",)


@admin.register(Document)
class DocumentAdmin(admin.ModelAdmin):
    list_display = ("title", "file")
    search_fields = ("title",)


@admin.register(Page)
class PageAdmin(admin.ModelAdmin):
    pass


@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ("name", "title")
    search_fields = ("name", "title")