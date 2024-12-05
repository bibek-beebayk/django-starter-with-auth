from django.contrib import admin
from .models import Link, SiteConfig, Person
from solo.admin import SingletonModelAdmin

admin.site.site_header = "Al Noor Admin"
admin.site.site_title = "Al Noor Admin Portal"

@admin.register(SiteConfig)
class SiteConfigAdmin(SingletonModelAdmin):
    fieldsets = [
        (
            "General",
            {
                "fields": (
                    "site_title",
                    "logo",
                    "government_license_number",
                    "company_registrar_number",
                    "pan",
                    "paid_up_capital",
                    "working_countries",
                    "mission",
                    "vision",
                )
            },
        ),
        (
            "Contact Info",
            {
                "fields": (
                    "address",
                    "phone_numbers",
                    "emails",
                    "website",
                    "social_links",
                )
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
