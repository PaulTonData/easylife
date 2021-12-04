from django.contrib.auth.models import User
from django.db import models
from django.template.defaultfilters import slugify

class Posting(models.Model):
    title = models.CharField(max_length=200)
    price = models.IntegerField()
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name="market_user")
    created = models.DateTimeField(auto_now_add=True)

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