from django.core.validators import MinValueValidator, MaxValueValidator
from django.db import models

class Place(models.Model):
    session_key = models.CharField(max_length=40)
    name = models.CharField("Name", max_length=200)
    description = models.TextField("Description")
    place_type = models.CharField("Type", max_length=100)
    address = models.CharField("Address", max_length=200, blank=True, null=True)
    rating = models.IntegerField(
        "Rating",
        validators=[MinValueValidator(1), MaxValueValidator(5)]
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def get_short_description(self):
        words = self.description.split(" ")
        if len(words) > 5:
            return " ".join(words[:5]) + "..."
        else:
            return self.description

    def get_rating(self):
        return "★" * self.rating + "☆" * (5 - self.rating)

    def __str__(self):
        return self.name
