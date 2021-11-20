from django.db import models

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

    def __str__(self):
        return self.title

class Photo(models.Model):
    posting = models.ForeignKey(Posting, on_delete=models.CASCADE)
    alt_text = models.CharField(max_length=200)
    blob = models.BinaryField()

    def __str__(self):
        return self.alt_text