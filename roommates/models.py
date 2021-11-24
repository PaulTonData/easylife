from django.contrib.auth.models import User
from django.db import models
from django.template.defaultfilters import slugify

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

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return f"/{self.id}/"


def get_image_filename(instance, filename):
    title = instance.posting.title
    slug = slugify(title)
    return "posting_images/%s-%s" % (slug, filename)

class Photo(models.Model):
    posting = models.ForeignKey(Posting, on_delete=models.CASCADE)
    alt_text = models.CharField(max_length=200, blank=True)
    image = models.ImageField(upload_to=get_image_filename,
                              verbose_name="Image", blank=True)

    def __str__(self):
        return self.alt_text