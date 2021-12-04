import os.path

from django.contrib.auth.models import User
from django.core.files.base import ContentFile
from django.db import models
from django.template.defaultfilters import slugify
from io import BytesIO
from PIL import Image

THUMB_SIZE = (200, 200)

class Posting(models.Model):
    WALKING = "WALK"
    BUS = "BUS"
    CAR = "CAR"
    RAIL = "RAIL"

    DISTANCE_MODE_CHOICES = [
        (WALKING, "walking"),
        (BUS, "by bus"),
        (CAR, "by car"),
        (RAIL, "by rail")
    ]

    title = models.CharField(max_length=200)
    rent = models.IntegerField()
    distance_time = models.IntegerField()
    distance_mode = models.CharField(
        max_length=20,
        choices=DISTANCE_MODE_CHOICES,
        default=WALKING)
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f"/{self.id}/"


def get_image_filename(instance, filename):
    title = instance.posting.title
    slug = slugify(title)
    return "posting_images/%s-%s" % (slug, filename)

def get_thumbnail_filename(instance, filename):
    title = instance.posting.title
    slug = slugify(title)
    return "posting_thumbnails/%s-%s" % (slug, filename)

class Photo(models.Model):
    posting = models.ForeignKey(Posting, on_delete=models.CASCADE)
    alt_text = models.CharField(max_length=200, blank=True)
    image = models.ImageField(upload_to=get_image_filename,
                              verbose_name="Image", blank=True)
    thumbnail = models.ImageField(upload_to=get_thumbnail_filename,
                             verbose_name="Thumbnail", blank=True)

    def save(self, *args, **kwargs):
        if not self.make_thumbnail():
            # set to default thumbnail
            raise Exception("Could not create thumbnail - is the file type valid?")

        super(Photo, self).save(*args, **kwargs)

    def make_thumbnail(self):
        image = Image.open(self.image)
        image.thumbnail(THUMB_SIZE, Image.ANTIALIAS)

        thumb_name, thumb_extension = os.path.splitext(self.image.name)
        thumb_extension = thumb_extension.lower()

        thumb_filename = thumb_name + '_thumb' + thumb_extension

        if thumb_extension in ['.jpg', '.jpeg']:
            FTYPE = 'JPEG'
        elif thumb_extension == '.gif':
            FTYPE = 'GIF'
        elif thumb_extension == '.png':
            FTYPE = 'PNG'
        else:
            return False # Unrecognized file type
    
        temp_thumb = BytesIO()
        image.save(temp_thumb, FTYPE)
        temp_thumb.seek(0)

        self.thumbnail.save(thumb_filename, ContentFile(temp_thumb.read()), save=False)
        temp_thumb.close()

        return True

    def __str__(self):
        return self.alt_text