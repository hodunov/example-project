from django.db import models

"""
Url shortener model
"""


class Shortener(models.Model):
    """
    Crates a short url base on the long url

    created -> Hour and Date
    time_followed -> times the link was followed
    long_url -> original link
    short_url -> shorted link https://yourdomain/(short_url)
    """

    created = models.DateTimeField(auto_now_add=True)
    times_followed = models.PositiveIntegerField(default=0)
    long_url = models.URLField()
    short_url = models.CharField(max_length=20, unique=True, blank=True)

    class Meta:
        ordering = ["-created"]

    def __str__(self):
        return f"{self.long_url} to {self.short_url}"

