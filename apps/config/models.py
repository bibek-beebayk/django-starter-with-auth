from django.db import models
# from core.libs.models import SingletonModel
from versatileimagefield.fields import VersatileImageField
from solo.models import SingletonModel
from django.contrib.postgres.fields import ArrayField
from django_ckeditor_5.fields import CKEditor5Field
from django.dispatch import receiver
from core.libs.images import warm

from core.libs.models import TimeStampModel


class Link(models.Model):
    title = models.CharField(max_length=255)
    logo = VersatileImageField(upload_to="images/social_logo/", blank=True, null=True)
    link = models.URLField(max_length=255)

    SIZES = {
        "logo": {
            "small": "thumbnail__320x180",
            "medium": "thumbnail__640x360",
        }
    }


    def __str__(self):
        return self.title
    


# class Address(models.Model):
#     title = models.CharField(max_length=255)
#     address = models.CharField(max_length=255)

#     def __str__(self):
#         return self.address

class SiteConfig(SingletonModel):

    # General Info
    site_title =  models.CharField(max_length=255, verbose_name="Company Name")
    government_license_number = models.CharField(max_length=255, blank=True, null=True)
    company_registrar_number = models.CharField(max_length=255, blank=True, null=True)
    pan = models.CharField(max_length=255, blank=True, null=True, verbose_name="PAN Number")
    paid_up_capital = models.PositiveBigIntegerField(blank=True, null=True, verbose_name="Paid Up Capital in Nepali Rupees")
    working_countries = ArrayField(models.CharField(max_length=255), blank=True, null=True)
    logo = VersatileImageField(upload_to="images/logo/", blank=True, null=True, verbose_name="Company Logo")
    mission = CKEditor5Field(config_name="extends", blank=True, null=True)
    vision = CKEditor5Field(config_name="extends", blank=True, null=True)

    # Contact Info
    phone_numbers = ArrayField(models.CharField(max_length=255), blank=True, null=True, help_text="Enter phone numbers separatedd by comma.")
    emails =  ArrayField(models.EmailField(), blank=True, null=True, help_text="Enter emails separated by comma.")
    # addresses = models.ManyToManyField(Address, blank=True)
    address = models.CharField(max_length=255, blank=True, null=True)
    website = models.URLField(max_length=1024, blank=True, null=True)
    social_links = models.ManyToManyField(Link, blank=True)
    google_maps_link = models.URLField(max_length=1024, blank=True, null=True)
    

    SIZES = {
        "logo": {
            "small": "thumbnail__320x180",
            "medium": "thumbnail__640x360",
        }
    }

    class Meta:
        verbose_name = "Company Details"
        verbose_name_plural = "Company Details"

    def __str__(self):
        return self.site_title
    

class Person(models.Model):
    # config = models.ForeignKey(SiteConfig, on_delete=models.CASCADE, related_name="people")
    position = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    email = models.EmailField(blank=True, null=True)
    mobile = models.CharField(max_length=255, blank=True, null=True)
    image = VersatileImageField(upload_to="images/people/", blank=True, null=True)
    message =  CKEditor5Field(config_name="extends", blank=True, null=True)

    SIZES = {
        "image": {
            "small": "thumbnail__320x180",
            "medium": "thumbnail__640x360",
        }
    }

    def __str__(self):
        return self.name
    
    class Meta:
        verbose_name_plural = "People"


class Client(models.Model):
    name = models.CharField(max_length=255)
    logo = VersatileImageField(upload_to="images/clients/", blank=True, null=True)

    SIZES = {
        "logo": {
            "small": "thumbnail__320x180",
            "medium": "thumbnail__640x360",
        }
    }


    def __str__(self):
        return self.name
    

class ContactUs(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField()
    phone = models.CharField(max_length=255)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
    
    class Meta:
        verbose_name_plural = "Contact Us"
    

class FAQ(models.Model):
    question = models.CharField(max_length=255)
    answer = CKEditor5Field(config_name="extends")

    def __str__(self):
        return self.question
    

class Document(TimeStampModel):
    title = models.CharField(max_length=255)
    file = models.FileField(upload_to="files/documents/")

    def __str__(self):
        return self.title
    

class Page(TimeStampModel):
    title = models.CharField(max_length=255)
    content = CKEditor5Field(config_name="extends")

    def __str__(self):
        return self.title
    

@receiver(models.signals.post_save, sender=Link)
@receiver(models.signals.post_save, sender=SiteConfig)
@receiver(models.signals.post_save, sender=Person)
@receiver(models.signals.post_save, sender=Client)
def warm_images(sender, instance, **kwargs):
    warm(instance)