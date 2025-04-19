from django.db import models


class Country(models.Model):
    name = models.CharField(max_length=20)


class City(models.Model):
    name = models.CharField(max_length=50)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)


class Hotel(models.Model):
    STAR_CHOICES = (("1", "1"), ("2", "2"), ("3", "3"), ("4", "4"), ("5", "5"))

    NUTRITION_TYPE_CHOICES = (
        ("BB", "BB"),
        ("HB", "HB"),
        ("FB", "FB"),
        ("AL", "AL"),
    )
    name = models.CharField(max_length=100)
    stars = models.CharField(choices=STAR_CHOICES)
    location = models.ForeignKey(City, on_delete=models.CASCADE)
    description = models.CharField(null=True)
    wifi = models.BooleanField(default=True)
    pool = models.BooleanField()
    nutrition_type = models.CharField(choices=NUTRITION_TYPE_CHOICES)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=["name", "location"], name="name_location")
        ]
