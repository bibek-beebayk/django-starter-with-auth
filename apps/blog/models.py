from django.db import models
from core.libs.models import TimeStampModel
from versatileimagefield.fields import VersatileImageField
from django_ckeditor_5.fields import CKEditor5Field
from django.dispatch import receiver
from core.libs.images import warm


class Post(TimeStampModel):
    title = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True)
    cover_image = VersatileImageField(upload_to="images/blog", blank=True, null=True)
    content = CKEditor5Field(config_name="extends")

    SIZES = {
        "cover_image": {
            "small": "thumbnail__320x180",
            "medium": "thumbnail__640x360",
        }
    }


    def __str__(self):
        return self.title


@receiver(models.signals.post_save, sender=Post)
def warm_images(sender, instance, **kwargs):
    warm(instance)